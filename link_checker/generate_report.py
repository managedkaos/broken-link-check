#!/usr/bin/env python
import re, sys

source = ''
broken = []

with open(sys.argv[1], 'r') as report:
    for line in report:
        if "Getting" in line:
            source = line.split()[-1]

        if "BROKEN" in line:
            broken.append(re.sub('├─BROKEN─ ', '', line.strip()))

        if "Finished!" in line and len(broken) > 0:
            print("# {}".format(source))
            print("|Broken Link|Error Code|")
            print("|----|----------|")
            for b in broken:
                link, code = b.split()
                print("|{}|{}|".format(link, code))
            print("|----|----------|")
            print()
            source = ''
            broken = []
