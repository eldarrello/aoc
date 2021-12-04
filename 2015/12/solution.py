def iter(l):
    total = 0
    for i in l:
        if isinstance(i, int):
            total += i
        if isinstance(i, dict):
            for k, v in i.items():
                if part_2 == True and (k == "red" or v == "red"):
                    i = {}
            total += iter(i.values())
        if isinstance(i, list):
            total += iter(i)
    return total

import json
s = json.loads(open('input.txt').read())
part_2 = False
print('Part 1:', iter(s))
part_2 = True
print('Part 2:', iter(s))