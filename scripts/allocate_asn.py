# scripts/allocate_asn.py
from pathlib import Path


ASN_FILE = Path("state/asn_last.txt")
ASN_MIN = 4200000000
ASN_MAX = 4294967294


last = int(ASN_FILE.read_text().strip())
next_asn = last + 1


if next_asn > ASN_MAX:
raise SystemExit("ASN pool exhausted")


ASN_FILE.write_text(str(next_asn))
print(next_asn)
