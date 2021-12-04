def find(s, o):
    for i in s:
        if i[1] == o:
            return i[0]

s = []
with open("input.txt") as f:
    for line in f:
        s.append(line.strip().split(')'))

count = 0
for i in s:
    count += 1;
    leaf = i[0]
    while leaf != "COM":
        leaf = find(s, leaf)
        count += 1
print(count)

