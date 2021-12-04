with open("input.txt") as f:
    s = f.read()
i = 0
min = 150
result = -1
image = [2] * 150
while True:
    l = s[i:i + 150]
    l = [int(a) for a in l]
    if l.count(0) < min:
        min = l.count(0)
        result = l.count(1) * l.count(2)
    for k in range(150):
        if image[k] == 2 and l[k] != 2:
            image[k] = l[k]
            
    i += 150
    if (i == len(s)):
        break
print(result)

i = 0
for y in range(6):
    print(image[i:i+25])
    i += 25
