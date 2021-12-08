s = open('input.txt').read().splitlines()
code = [[0,2,3,4,5,6],[4,6],[0,1,2,4,5],[0,1,2,4,6],[1,3,4,6],[0,1,2,3,6],[0,1,2,3,5,6],[0,4,6],[0,1,2,3,4,5,6],[0,1,2,3,4,6]]
total = 0
h = 10 * [0]
for x in s:
    input, output = x.split(' | ')
    for i in input.split( ):
        if len(i) == 2:
            one = i
        if len(i) == 4:
            four = i
    map = {}
    for i in "abcdefg":
        c = input.count(i)
        map[i] = [5,0,3,2,0,6][c - 4]
        if c == 8 and i in one:
            map[i] = 4
        elif c == 7 and i in four:
            map[i] = 1
    v = 0
    for i in output.split( ):
        h[len(i)] += 1
        v = v * 10 + code.index(sorted([map[k] for k in i]))
    total += v
print("Part 1:", h[2] + h[4] + h[3] + h[7])
print("Part 2:", total)

'''
 0000
3    4
3    4
 1111
5    6
5    6
 2222

counts:
8->0,4
7->1,2
6->3
4->5
9->6
'''
