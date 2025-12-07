s = open('input.txt').read().splitlines()
m = {(y, x) for y in range(len(s)) for x in range(len(s[0])) if s[y][x] == '^'}
beams = {s[0].index('S'): 1}
splits = 0
for y in range(1, len(s)):
    nbeams = {}
    for x, c in beams.items():
        if (y, x) in m:
            splits += 1
            nbeams[x - 1] = (nbeams[x - 1] if (x - 1) in nbeams else 0) + c
            nbeams[x + 1] = (nbeams[x + 1] if (x + 1) in nbeams else 0) + c
        else:
            nbeams[x] = (nbeams[x] if x in nbeams else 0) + c
    beams = nbeams
print("Part 1:", splits)
print("Part 2:", sum([c for c in beams.values()]))

