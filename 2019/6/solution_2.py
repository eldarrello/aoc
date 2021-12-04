def find(s, o):
    for i in s:
        if i[1] == o:
            return i[0]
def path(s, o):
    p = []
    while o != "COM":
        o = find(s, o)
        p.append(o)
    return p

s = []
with open("input.txt") as f:
    for line in f:
        s.append(line.strip().split(')'))

p1 = path(s,'YOU')
p2 = path(s,'SAN')

for i in p1:
    if p2.count(i):
        print(p1.index(i) + p2.index(i))
        break
