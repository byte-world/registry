#!/usr/bin/env bash
set -e

echo "=== Byte World Onboarding Tool ==="

read -rp "Full name / handle: " NAME
read -rp "Email address: " EMAIL
read -rp "ASN (e.g. 4200001234): " ASN
read -rp "Short identifier (e.g. USER1): " TAG
read -rp "PGP fingerprint: " PGP
read -rp "Create AS-SET? (y/n): " CREATE_ASSET

BASE="../../registry"

PERSON_ID="BW-PERSON-${ASN}"
MNT="BW-MNT-${TAG}"

mkdir -p \
  "$BASE/person" \
  "$BASE/mntner" \
  "$BASE/asn" \
  "$BASE/peering" \
  "$BASE/as-set"

# PERSON
cat > "$BASE/person/$PERSON_ID" <<EOF
person:         $NAME
nic-hdl:        $PERSON_ID
email:          $EMAIL
mnt-by:         $MNT
source:         BYTEWORLD
EOF

# MNTNER
cat > "$BASE/mntner/$MNT" <<EOF
mntner:         $MNT
admin-c:        $PERSON_ID
tech-c:         $PERSON_ID
auth:           pgp-fingerprint $PGP
mnt-by:         $MNT
source:         BYTEWORLD
EOF

# AUT-NUM
cat > "$BASE/asn/AS$ASN" <<EOF
aut-num:        AS$ASN
as-name:        ${TAG}-NET
admin-c:        $PERSON_ID
tech-c:         $PERSON_ID
mnt-by:         $MNT
import:         from AS4200000000 accept ANY
export:         to AS4200000000 announce AS$ASN
remarks:        Byte World participant
source:         BYTEWORLD
EOF

# PEERING
cat > "$BASE/peering/AS$ASN.md" <<EOF
# Peering information for AS$ASN

Operator: $NAME  
Email: $EMAIL  

Preferred tunnel: WireGuard  
IPv6 supported: Yes  

Notes:
- Open peering
EOF

# AS-SET (optional)
if [[ "$CREATE_ASSET" == "y" ]]; then
  cat > "$BASE/as-set/AS-${TAG}" <<EOF
as-set:         AS-${TAG}
members:        AS$ASN
mnt-by:         $MNT
source:         BYTEWORLD
EOF
fi

echo "✔ Onboarding objects created successfully"
echo "➡ Review files, then commit & open a PR"
