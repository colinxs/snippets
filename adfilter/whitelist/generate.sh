#!/usr/bin/env bash

DIR="$(dirname $0)"
DOMAINS="${DIR}/domains.txt"
ADGUARD="${DIR}/adguard.txt"

cat <<EOF > "$ADGUARD"
! Title: Personal Whitelist 
! Description: Whitlisted domains in ADP Syntax
EOF

while read -r domain; do 
    echo "@@||$domain" >> "$ADGUARD"
done < "$DOMAINS" 
