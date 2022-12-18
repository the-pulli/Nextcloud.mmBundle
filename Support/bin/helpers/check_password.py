#!/usr/bin/env python3

import re
import sys

password = sys.argv[1]

matching1 = re.compile(r"[a-z]+")
matching2 = re.compile(r"[A-Z]+")
matching3 = re.compile(r"[0-9]+")
matching4 = re.compile(r"[!@#$%^&*()_+\-=\[\]{};':|,.<>/?\"]+")

matches = [matching1, matching2, matching3, matching4]

result = []
for match in matches:
    result.append(match.findall(password))

print(all(map(lambda m: True if len(m) >= 1 else False, result)))
