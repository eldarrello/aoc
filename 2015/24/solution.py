import itertools
s = open('input.txt').read().splitlines()
s = [int(x) for x in s]

def find(n, m):
    target = int(sum(s) / n)
    t = list(itertools.combinations(s, m))
    min_qe = 1000000000000
    for i in t:
        if sum(i) == int(target):
            ack = 1
            for k in i:
                ack *= k
            if ack < min_qe:
                min_qe = ack
    return min_qe

print('Part 1:', find(3, 6))
print('Part 2:', find(4, 5))
