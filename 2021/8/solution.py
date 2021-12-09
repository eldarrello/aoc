s = open('input.txt').read().splitlines()
total = 0
h = 10 * [0]
for x in s:
    input, output = x.split(' | ')
    mm = {[1, 7, 4, 0, 9, 8][len(i) - 2]:sorted(i) for i in input.split( )}
    for i in input.split( ):
        i = sorted(i)
        if len(i) == 5: #2, 3, 5
            mm[3 if set(mm[1]).issubset(set(i)) else 2 if len(set(i + mm[4])) == 7 else 5] = i
        if len(i) == 6: #6, 9, 0
            mm[9 if set(mm[4]).issubset(i) else 0 if set(mm[1]).issubset(i) else 6] = i
    v = 0
    for i in output.split( ):
        h[len(i)] += 1
        v = v * 10 + [mm[i] for i in range(10)].index(sorted(i))
    total += v
print("Part 1:", h[2] + h[4] + h[3] + h[7])
print("Part 2:", total)
