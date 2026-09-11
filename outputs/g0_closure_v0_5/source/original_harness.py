#!/usr/bin/env python3
"""Anticipatory Execution G0 deterministic extraction QA harness.

Run in an environment with torch + transformers and access to the frozen model.
Primary target: Qwen/Qwen2.5-7B-Instruct.

This script does NOT train or evaluate the research hypothesis. It only validates
that hidden-state extraction is reproducible enough to unblock Stage 1.
"""

from __future__ import annotations
import argparse, hashlib, json, math, os, platform, random, sys, time
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, __version__ as transformers_version


QA_TEXTS = [
    "Research U.S. manufacturers of robotic actuators",
    "Find an Italian restaurant near my hotel with outdoor seating",
    "Schedule a 30-minute meeting with Alex next week",
    "Write a Python function to parse the log file and return error counts",
    "Compare QQQ and DIA downside scenarios for a seven percent decline",
    "Turn on the living-room lights at thirty percent",
    "Find papers on frozen-model hidden states for predicting future intent",
    "Draft an email thanking the recruiter for the consideration",
]

@dataclass
class Check:
    name: str
    status: str
    max_abs_diff: float | None = None
    mean_abs_diff: float | None = None
    detail: str = ""


def set_deterministic(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)
    torch.use_deterministic_algorithms(True, warn_only=True)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False


def tensor_checksum(t: torch.Tensor) -> str:
    a = t.detach().to(torch.float32).cpu().contiguous().numpy()
    return hashlib.sha256(a.tobytes()).hexdigest()


def compare(a: torch.Tensor, b: torch.Tensor, atol: float, rtol: float) -> Tuple[bool, float, float]:
    a = a.detach().to(torch.float32).cpu()
    b = b.detach().to(torch.float32).cpu()
    d = (a - b).abs()
    ok = torch.allclose(a, b, atol=atol, rtol=rtol)
    return ok, float(d.max().item()), float(d.mean().item())


def load(model_id: str, revision: str | None, dtype: str, device: str):
    tok = AutoTokenizer.from_pretrained(model_id, revision=revision, use_fast=True)
    if tok.pad_token_id is None:
        tok.pad_token = tok.eos_token
    dtype_obj = {"float32": torch.float32, "float16": torch.float16, "bfloat16": torch.bfloat16}[dtype]
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        revision=revision,
        torch_dtype=dtype_obj,
        low_cpu_mem_usage=True,
    ).to(device)
    model.eval()
    return tok, model


def extract(tok, model, texts: List[str], device: str, pad_to: int | None = None):
    enc = tok(
        texts,
        return_tensors="pt",
        padding=True if len(texts) > 1 or pad_to else False,
        truncation=False,
        max_length=None,
    )
    if pad_to:
        cur = enc["input_ids"].shape[1]
        if cur < pad_to:
            add = pad_to - cur
            pad_ids = torch.full((enc["input_ids"].shape[0], add), tok.pad_token_id, dtype=enc["input_ids"].dtype)
            pad_mask = torch.zeros((enc["attention_mask"].shape[0], add), dtype=enc["attention_mask"].dtype)
            enc["input_ids"] = torch.cat([enc["input_ids"], pad_ids], dim=1)
            enc["attention_mask"] = torch.cat([enc["attention_mask"], pad_mask], dim=1)
    enc = {k: v.to(device) for k, v in enc.items()}
    with torch.inference_mode():
        out = model(**enc, output_hidden_states=True, use_cache=False, return_dict=True)
    return enc, out


def last_active_hidden(enc, out, layer: int) -> torch.Tensor:
    h = out.hidden_states[layer]
    idx = enc["attention_mask"].sum(dim=1) - 1
    return torch.stack([h[i, int(idx[i]), :] for i in range(h.shape[0])], dim=0)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model-id", default=os.getenv("MODEL_ID", "Qwen/Qwen2.5-7B-Instruct"))
    ap.add_argument("--revision", default=os.getenv("MODEL_REVISION"))
    ap.add_argument("--dtype", choices=["float32","float16","bfloat16"], default="bfloat16")
    ap.add_argument("--device", default="cuda" if torch.cuda.is_available() else "cpu")
    ap.add_argument("--seed", type=int, default=1729)
    ap.add_argument("--atol", type=float, default=1e-5)
    ap.add_argument("--rtol", type=float, default=1e-5)
    ap.add_argument("--output", default="g0_qa_report.json")
    args = ap.parse_args()

    set_deterministic(args.seed)
    tok, model = load(args.model_id, args.revision, args.dtype, args.device)
    n_layers = model.config.num_hidden_layers
    probe_layers = sorted(set([1, max(1,n_layers//4), max(1,n_layers//2), max(1,3*n_layers//4), n_layers]))
    checks: List[Check] = []

    # 1) exact repeat within one model instance
    for layer in probe_layers:
        e1, o1 = extract(tok, model, [QA_TEXTS[0]], args.device)
        e2, o2 = extract(tok, model, [QA_TEXTS[0]], args.device)
        a, b = last_active_hidden(e1,o1,layer), last_active_hidden(e2,o2,layer)
        ok, mx, mn = compare(a,b,args.atol,args.rtol)
        checks.append(Check(f"repeat_layer_{layer}", "PASS" if ok else "FAIL", mx, mn))

    # 2) batch vs singleton equivalence
    eb, ob = extract(tok, model, QA_TEXTS[:4], args.device)
    for i, text in enumerate(QA_TEXTS[:4]):
        es, os_ = extract(tok, model, [text], args.device)
        for layer in probe_layers:
            bh = last_active_hidden(eb,ob,layer)[i:i+1]
            sh = last_active_hidden(es,os_,layer)
            ok, mx, mn = compare(bh,sh,args.atol,args.rtol)
            checks.append(Check(f"batch_vs_single_{i}_layer_{layer}", "PASS" if ok else "FAIL", mx, mn))

    # 3) masked-padding invariance at fixed tensor shape
    text = QA_TEXTS[1]
    e3, o3 = extract(tok, model, [text], args.device, pad_to=96)
    e4, o4 = extract(tok, model, [text], args.device, pad_to=96)
    # Replace only masked token IDs; attention mask remains zero on those positions.
    masked = e4["attention_mask"] == 0
    if masked.any():
        e4["input_ids"][masked] = int((tok.eos_token_id or 1) + 1) % int(model.config.vocab_size)
        with torch.inference_mode():
            o4 = model(**e4, output_hidden_states=True, use_cache=False, return_dict=True)
    for layer in probe_layers:
        a, b = last_active_hidden(e3,o3,layer), last_active_hidden(e4,o4,layer)
        ok, mx, mn = compare(a,b,args.atol,args.rtol)
        checks.append(Check(f"masked_padding_invariance_layer_{layer}", "PASS" if ok else "FAIL", mx, mn,
                            "Changing masked token IDs must not change active-prefix state."))

    # 4) reload equivalence
    ref_enc, ref_out = extract(tok, model, [QA_TEXTS[2]], args.device)
    ref = {l: last_active_hidden(ref_enc,ref_out,l).detach().cpu() for l in probe_layers}
    del model
    if torch.cuda.is_available(): torch.cuda.empty_cache()
    tok2, model2 = load(args.model_id, args.revision, args.dtype, args.device)
    enc_r, out_r = extract(tok2, model2, [QA_TEXTS[2]], args.device)
    for layer in probe_layers:
        b = last_active_hidden(enc_r,out_r,layer)
        ok, mx, mn = compare(ref[layer],b,args.atol,args.rtol)
        checks.append(Check(f"reload_layer_{layer}", "PASS" if ok else "FAIL", mx, mn))

    # 5) sequence-length extension diagnostic (NOT a validity invariant).
    # The same visible prefix is run in tensors of two different padded lengths.
    # Differences are recorded but do not independently fail G0 because kernels can vary with shape.
    e_short, o_short = extract(tok2, model2, [QA_TEXTS[3]], args.device, pad_to=64)
    e_long, o_long = extract(tok2, model2, [QA_TEXTS[3]], args.device, pad_to=128)
    for layer in probe_layers:
        a, b = last_active_hidden(e_short,o_short,layer), last_active_hidden(e_long,o_long,layer)
        ok, mx, mn = compare(a,b,args.atol,args.rtol)
        checks.append(Check(f"length_extension_diag_layer_{layer}", "INFO", mx, mn,
                            "Diagnostic only; compare magnitude to tolerance and document kernel/shape sensitivity."))

    blocking = [c for c in checks if c.status == "FAIL"]
    report = {
        "gate": "G0 Instrumentation",
        "status": "PASS" if not blocking else "FAIL",
        "model_id": args.model_id,
        "revision": args.revision,
        "dtype": args.dtype,
        "device": args.device,
        "seed": args.seed,
        "tolerances": {"atol": args.atol, "rtol": args.rtol},
        "probe_layers_hidden_state_tuple_indices": probe_layers,
        "environment": {
            "python": sys.version,
            "platform": platform.platform(),
            "torch": torch.__version__,
            "transformers": transformers_version,
            "cuda_available": torch.cuda.is_available(),
            "gpu": torch.cuda.get_device_name(0) if torch.cuda.is_available() else None,
        },
        "blocking_failures": [asdict(c) for c in blocking],
        "checks": [asdict(c) for c in checks],
        "notes": [
            "Hidden-state tuple index 0 is embedding output; final index is post-final transformer block.",
            "Length-extension checks are diagnostic, not blocking invariants.",
            "Any blocking failure must be resolved before Stage 1 feature extraction.",
        ],
    }
    Path(args.output).write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps({"status":report["status"],"blocking_failures":len(blocking),"output":args.output}, indent=2))
    sys.exit(0 if not blocking else 2)

if __name__ == "__main__":
    main()
