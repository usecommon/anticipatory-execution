# Preserved preparation failure

preparation_01 failed after creating payload/opportunity files, before generating candidates or running early actions. Freeze construction attempted to express a relative CLI output path against an absolute package root. The ValueError traceback, partial artifacts and original run.py are retained.

Recovery resolves the preparation output path before creating relative manifest entries. It also verifies and pins the existing public adapter source chain explicitly. No candidate rule, scheduled opportunity, source selection, task specification, label or outcome changed. preparation_02 is a separate attempt; compare its payload/opportunity bytes to the preserved first attempt. No outcome was available when recovery was made.
