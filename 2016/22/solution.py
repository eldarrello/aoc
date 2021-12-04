import re
s = open('input.txt').read().splitlines()
nodes = []
max_x = 0
max_y = 0
for i in range(2, len(s)):
    w = s[i].split()
    x, y = re.search('-x(\d+)-y(\d+)', w[0]).groups()
    if int(x) > max_x : max_x = int(x)
    if int(y) > max_y: max_y = int(y)
    nodes.append((int(w[2].strip('T')), int(w[3].strip('T')), (x, y)))  #used, available
count = 0
for i in nodes:
    if i[0] == 0:
        #print("G", i)
        continue
    can_move = False
    for j in nodes:
        if i[0] <= j[1] and i != j:
            count += 1
            can_move = True
    if not can_move:
        #print("B", i)
        pass
print("Part 1:", count)

'''
Todo::solve part 2 programmatically
visual insight: #30x32 = 990 cells, 960 are movable, blockers are all on row 27
x: 15->3 = 12       move empty cell around blockers
y:29->0  = 29       stright up
x:3->31  = 28       left to the G
31 * 5 + 1 = 156    fetch G
'''
print("Part 2:", 12 + 29 + 28 + 31 * 5 + 1)