```sh
#!/usr/bin/env bash
# scripts/onboard.sh


ASN=$(python3 scripts/allocate_asn.py)
V4=$(python3 scripts/allocate_ipv4.py)
V6=$(python3 scripts/allocate_ipv6.py)


python3 scripts/generate_objects.py <<EOF
$ASN
$USER
$USER@example.com
$V4
$V6
EOF


echo "Allocated ASN: AS$ASN"
echo "IPv4: $V4"
echo "IPv6: $V6"
```
