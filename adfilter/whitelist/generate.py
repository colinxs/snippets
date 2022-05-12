#!/usr/bin/env python3

from pathlib import Path
import re

SCRIPT = Path(__file__).parent.absolute()
DOMAINS = SCRIPT.joinpath('domains.txt')
ADGUARD = SCRIPT.joinpath('adguard.txt')

DOMAIN_PATTERN = re.compile(r'^((([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9]))$')
COMMENT_PATTERN = re.compile(r'^\s*\!\s*(.*)$')

with open(DOMAINS, 'r', encoding="utf-8") as domains:
    with open(ADGUARD, 'w', encoding="utf-8") as adguard:
        for line in domains:
            m = re.match(DOMAIN_PATTERN, line)
            if m:
                adguard.write(f'@@||{m.group(1)}\n')
                continue
            
            m = re.match(COMMENT_PATTERN, line)
            if m:
                adguard.write(f'! {m.group(1)}\n')
                continue

            print(f'Invalid domain: {line}')

