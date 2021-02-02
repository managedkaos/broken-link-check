#!/usr/bin/env python
import re, sys

source = ''
broken = []
count  = 0

print("|#|Source|Broken Link|Error Code|")
print("|-|------|-----------|----------|")

with open(sys.argv[1], 'r') as report:
    for line in report:
        if "Getting" in line:
            source = line.split()[-1]

        if "BROKEN" in line:
            broken.append(re.sub('├─BROKEN─ ', '', line.strip()))

        if "Finished!" in line and len(broken) > 0:
            for b in broken:
                count = count + 1
                link, code = b.split()
                print("|{}|{}|{}|{}|".format(count, source, link, code))
            print()
            source = ''
            broken = []
