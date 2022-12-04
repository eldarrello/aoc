s = open('input.txt').read().splitlines()
ac1 = 0
ac2 = 0
for i in s:
    a1, a2, b1, b2 = list(map(int, i.replace(',', '-').split('-')))
    if (a1 >= b1 and a2 <= b2) or (b1 >= a1 and b2 <= a2):
        ac1 += 1
    if (a1 >= b1 and a1 <= b2) or (b1 >= a1 and b1 <= a2):
        ac2 += 1
print("Part 1:", ac1)
print("Part 2:", ac2)