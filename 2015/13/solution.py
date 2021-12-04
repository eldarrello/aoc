s = open('input.txt').read().splitlines()

def eval(c):
    score = 0
    for i in range(-1, len(c) - 1):
        if c[i] == "X" or c[i + 1] == "X": continue
        score += scores[(c[i], c[i + 1])]
        score += scores[(c[i + 1], c[i])]
    return score

guys = set()
scores = {}
for i in s:
    k = i.split()
    k[10] = k[10].replace('.', '')
    guys.add(k[0])
    scores[(k[0], k[10])] = int(k[3]) if k[2] == "gain" else -int(k[3])

import itertools
def eval_all():
    perms = itertools.permutations(guys)
    best_score = 0
    for i in perms:
        score = eval(i)
        if score > best_score:
            best_score = score
    return best_score

print('Part 1:', eval_all())
guys.add('X')
print('Part 2:', eval_all())