s = open('input.txt').read().splitlines()
vs = [[int(i.split()[1]) for i in l.split(': ')[1].split(', ')] for l in s]
c = 4 * [0]
max_score_1 = 0
max_score_2 = 0
for c[0] in range(101):
    for c[1] in range(101 - c[0]):
        for c[2] in range(101 - c[1] - c[0]):
            for c[3] in range(101 - c[2] - c[1] - c[0]):
                test = 1
                for t in range(4):
                    acc = sum([c[i] * vs[i][t] for i in range(4)])
                    acc = max(0, acc)
                    test *= acc
                max_score_1 = max(max_score_1, test)
                if sum([c[i] * vs[i][4] for i in range(4)]) == 500:
                    max_score_2 = max(max_score_2, test)
print('Part 1:', max_score_1)
print('Part 2:', max_score_2)
# Does full search, which takes < 20 sec to run. So no real need for inventing something more complex.