# scripts/generate_objects.py
from pathlib import Path


asn = input("ASN: ")
name = input("Name: ")
email = input("Email: ")
v4 = input("IPv4 prefix: ")
v6 = input("IPv6 prefix: ")


(Path(f"person/BW-PERSON-{asn}")
.write_text(f"""
person: {name}
nic-hdl: BW-PERSON-{asn}
email: {email}
source: BYTEWORLD
"""))


(Path(f"asn/AS{asn}")
.write_text(f"""
aut-num: AS{asn}
as-name: {name.upper()}-NET
admin-c: BW-PERSON-{asn}
tech-c: BW-PERSON-{asn}
import: from AS4200000000 accept ANY
export: to AS4200000000 announce AS{asn}
source: BYTEWORLD
"""))
