s = open('input.txt').read().splitlines()
state = list(s[0].split(': ')[1])
rules = []
for i in range(2, len(s)):
    rules.append(s[i].split(' => '))
for i in range(10):
    state.insert(0, '.')
    state.append('.')

def gen(g):
    global state
    #print(g, ''.join(state))
    state.insert(0, '.')
    state.insert(0, '.')
    state.append('.')
    state.append('.')
    state.append('.')
    new_state = []
    for i in range(len(state) - 4):
        had_rule = False    # This was needed only for the example.
        for r in rules:
            for x in range(5):
                if r[0][x] != state[i + x]:
                    break
            else:
                new_state.append(r[1])
                had_rule = True
                break
        if had_rule == False:
            new_state.append('.')
    state = new_state
    score = 0
    for i in range(len(state)):
        if state[i] == '#':
            score += i - 10
    return score

for g in range(1, 102):     # 102 - just found out it starts to repeat from 102
    score = gen(g)
    if g == 20:
        print("Part 1:", score)
g += 1
next_score = gen(g)
part_2 = next_score + (50000000000 - g) * (next_score - score)
print("Part 2:", part_2)
