import operator
s = open('input.txt').read().splitlines()
r = {}
ops = { ">": operator.gt, "<": operator.lt, ">=": operator.ge, "<=": operator.le, "==": operator.eq, "!=": operator.ne , "inc": operator.add, "dec": operator.sub } # etc.
part_2 = 0
for i in s:
    ws = i.split(' ') #lzd inc 958 if m <= 2069
    if ws[4] not in r:
        r[ws[4]] = 0
    if ws[0] not in r:
        r[ws[0]] = 0
    if ops[ws[5]](r[ws[4]], int(ws[6])):
        r[ws[0]] = ops[ws[1]](r[ws[0]], int(ws[2]))
        part_2 = max(part_2, r[ws[0]])
max_value = 0
for r, value in r.items():
    max_value = max(max_value, value)
print("Part 1:", max_value)
print("Part 2:", part_2)
