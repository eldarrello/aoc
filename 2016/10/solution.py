s = open('input.txt').read().splitlines()
bots = {}
out = {}
def store(n, v):
    if n in bots:
        bots[n].append(v)
    else:
        bots[n] = [v]
def do():
    for ss in s:
        w = ss.split()
        if len(w) != 6 and w[1] in bots and len(bots[w[1]]) > 1:
            vs = sorted(bots[w[1]])
            if 17 in vs and 61 in vs:
                print('Part 1:', w[1])
            if w[5] == 'bot':
                store(w[6], vs[0])
            else:
                out[w[6]] = vs[0]
            if w[10] == 'bot':
                store(w[11], vs[-1])
            else:
                out[w[11]] = vs[-1]
            bots[w[1]] = []

for ss in s:
    w = ss.split()
    if len(w) == 6:
        store(w[5], int(w[1]))
while not('0' in out and '1' in out and '2' in out):
    do()

print('Part 2:', out['0'] * out['1'] * out['2'])