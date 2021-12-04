s = open('input.txt').read().splitlines()
incs = []
for i in s:
    k = i.replace(',', '').split()
    nums = []
    for j in k:
        if j.lstrip('-').isdigit():
            nums.append(int(j))
    incs.append(nums)

def eval(mix):
    total = 1
    for k in range(4):
        sub_total = 0
        for i in range(len(incs)):
            sub_total += mix[i] * incs[i][k]
        if sub_total < 0:
            return 0, 0
        total *= sub_total
    cal = 0
    for i in range(len(incs)):
        cal += mix[i] * incs[i][4]
    return total, cal

import random

def get_mix():
    mix = []
    for i in range(3):
        mix.append(random.randrange(0, 100 - sum(mix)))
    mix.append(100 - sum(mix))
    return mix

best_score_1 = 0
best_score_2 = 0
for i in range(1000000):
    score, cal = eval(get_mix())
    best_score_1 = max(best_score_1, score)
    if cal == 500:
        best_score_2 = max(best_score_2, score)
print('Part 1:', best_score_1)
print('Part 2:', best_score_2)

#todo::deterministic way of generating permutations?