m = {'AX': (4, 3), 'AY': (8, 4), 'AZ': (3, 8), 'BX': (1, 1), 'BY': (5, 5), 'BZ': (9, 9), 'CX': (7, 2), 'CY': (2, 6), 'CZ': (6, 7) }
k = list(zip(*[m[i[0] + i[2]] for i in open('input.txt').read().splitlines()]))
print("Part 1:", sum(k[0]))
print("Part 2:", sum(k[1]))