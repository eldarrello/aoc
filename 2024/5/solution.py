def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j + 1] in m and arr[j] in m[arr[j + 1]]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
a, b = open('input.txt').read().split("\n\n")
acc = 0
acc2 = 0
m = {}
for i in a.splitlines():
    c, d = i.split('|')
    if c not in m:
        m[c] = [d]
    else:
        m[c].append(d)
for i in b.splitlines():
    vs = i.split(',')
    q = bubble_sort(list(vs))
    if vs == q:
        acc += int(q[len(q) // 2])
    else:
        acc2 += int(q[len(q) // 2])

print("Part 1:", acc)
print("Part 2:", acc2)

