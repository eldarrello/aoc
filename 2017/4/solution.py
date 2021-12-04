s = open('input.txt').read().splitlines()
count_1 = 0
count_2 = 0
for i in s:
    words = i.split(' ')
    map = {}
    list_2 = []
    count_1 += 1
    count_2 += 1
    for word in words:
        if word in map:
            count_1 -= 1
            break
        else:
            map[word] = 1
    for word in words:
        m = ''.join(sorted(word))
        if m in list_2:
            count_2 -= 1
            break
        else:
            list_2.append(m)
print("Part 1:", count_1)
print("Part 2:", count_2)