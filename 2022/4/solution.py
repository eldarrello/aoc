r = [list(map(int, i.replace(',', '-').split('-'))) for i in open('input.txt').read().splitlines()]
print("Part 1:", sum([(a1 >= b1 and a2 <= b2) or (b1 >= a1 and b2 <= a2) for a1, a2, b1, b2 in r]))
print("Part 2:", sum([(a1 >= b1 and a1 <= b2) or (b1 >= a1 and b1 <= a2) for a1, a2, b1, b2 in r]))