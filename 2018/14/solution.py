e1 = 0
e2 = 1
r = [3,7]
z = [0, 4, 7, 8, 0, 1]
while(len(r) < 47801 + 10 + 100000000):
    sum = r[e1] + r[e2]
    if sum >= 10:
        r.append(1)
    r.append(sum % 10)
    e1 += 1 + r[e1]
    e1 %= len(r)
    e2 += 1 + r[e2]
    e2 %= len(r)
    if r[-6:] == z or r[-7:-1] == z:
        l = 7 if r[-7:-1] == z else 6
        print("Part 2:", len(r) - l)
        break
print("Part 1:", ''.join([str(i) for i in r[47801:47801 + 10]]))

