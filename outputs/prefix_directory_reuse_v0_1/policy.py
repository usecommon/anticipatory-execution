"""Pure authored candidate rule. No file/environment/network reads."""
import json
import re
import sys
SCHEMA='ls(a: bool = false) -> current_directory_content; operates only on cwd'

def propose(payload):
    if type(payload) is not dict or set(payload)!={'prefix','cwd','tool_schema'}:
        raise ValueError('exact prefix/cwd/schema payload required')
    if any(type(payload[k]) is not str or not payload[k] for k in payload):
        raise ValueError('nonempty strings required')
    if payload['tool_schema']!=SCHEMA:raise ValueError('unknown schema')
    words=set(re.findall(r'\w+',payload['prefix'].lower()))
    if not(words & {'list','listing'} and words & {'file','files','directory','directories'}):
        return {'status':'abstain','reason':'no_supported_listing_trigger','candidate':None}
    target=words & {'tmp','temp','temporary'}
    base=payload['cwd'].rstrip('/').split('/')[-1]
    if target and not any(t==base or t=='temporary' and base in {'tmp','temp'} for t in target):
        return {'status':'abstain','reason':'recognized_target_requires_unsupported_navigation','candidate':None}
    hidden=not bool(re.search(r'\bdo\s+not\s+list\s+hidden\b',payload['prefix'],re.I))
    return {'status':'proposed','reason':'observed_listing_trigger','candidate':{'operation':'ls','directory':payload['cwd'],'a':hidden}}

if __name__=='__main__':
    for line in sys.stdin:
        print(json.dumps(propose(json.loads(line))))
