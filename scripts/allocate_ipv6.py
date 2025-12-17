# scripts/allocate_ipv6.py
import ipaddress, json
from pathlib import Path


STATE = Path("state/ipv6_pool.json")
data = json.loads(STATE.read_text())
pool = ipaddress.IPv6Network(data["pool"])
allocated = [ipaddress.IPv6Network(p) for p in data["allocated"]]


for subnet in pool.subnets(new_prefix=32):
if subnet not in allocated:
allocated.append(subnet)
data["allocated"] = [str(n) for n in allocated]
STATE.write_text(json.dumps(data, indent=2))
print(subnet)
break
else:
raise SystemExit("IPv6 pool exhausted")
