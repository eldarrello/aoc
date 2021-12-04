s = open('input.txt').read().splitlines()
k = [tuple(i.split('/')) for i in s]
nodes = [[('0', '0')]]
max_score = 0
max_len = 0
max_len_score = 0
while nodes:
    node = nodes.pop(0)
    found = False
    for i in k:
        if i in node or (i[1], i[0]) in node:
            continue
        if i[0] == node[-1][1]:
            n = list(tuple(node))
            n.append(i)
            nodes.append(n)
            found = True
        elif i[1] == node[-1][1]:
            n = list(tuple(node))
            n.append((i[1], i[0]))
            nodes.append(n)
            found = True
    if not found:
        score = sum(int(i[0]) + int(i[1]) for i in node)
        if score > max_score:
            max_score = score
        if len(node) > max_len or (len(node) == max_len and score > max_len_score):
            max_len = len(node)
            max_len_score = score

print("Part 1:", max_score) #todo::too slow! Brute force runs a minute or so!
#One way to make it faster is to instead of keeping used ports to keep remaining ports and update max len and max score on each iteration.
print("Part 2:", max_len_score)
