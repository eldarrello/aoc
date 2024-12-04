s = open('input.txt').read().splitlines()
m = {(x, y): s[y][x] for y in range(len(s)) for x in range(len(s[0]))}
print("Part 1:", sum([''.join([m[(kx, ky)] for kx, ky in [(x + dx * t, y + dy * t) for t in range(4)] if (kx, ky) in m]) == 'XMAS' for x, y in m.keys() for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (1, -1), (-1, 1)]]))
print("Part 2:", sum([m[(x, y)] == 'A' and ''.join([m[(x + dx, y + dy)] for dx, dy in [(-1, -1), (1, 1), (1, -1), (-1, 1)] if (x + dx, y + dy) in m]) in ['MSMS', 'MSSM', 'SMSM', 'SMMS'] for x, y in m.keys()]))