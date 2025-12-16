#!/usr/bin/env bash
set -e

echo "=== Byte World Registry Validator ==="

ERRORS=0

check_file () {
  if ! grep -q "source:[[:space:]]*BYTEWORLD" "$1"; then
    echo "❌ Missing source in $1"
    ERRORS=$((ERRORS+1))
  fi
}

for f in ../../registry/{person,mntner,asn,inetnum,inet6num,route,route6}/*; do
  [[ -f "$f" ]] && check_file "$f"
done

if [[ $ERRORS -eq 0 ]]; then
  echo "✔ Registry validation passed"
else
  echo "❌ Validation failed with $ERRORS errors"
  exit 1
fi
