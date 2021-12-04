s = open('input.txt').read().splitlines()

def sec():
    for i in map:
        if fly_count[i] > 0:
            dist[i] += map[i][0]
            fly_count[i] -= 1
        else:
            wait_count[i] -= 1
            if wait_count[i] == 0:
                fly_count[i] = map[i][1]
                wait_count[i] = map[i][2]
    for i in winners():
        score[i] += 1

def winners():
    best = 0
    winners = []
    for i in dist:
        if dist[i] > best:
            winners = [i]
            best = dist[i]
        elif dist[i] == best:
            winners.append(i)
    return winners

map = {}
dist = {}
fly_count = {}
wait_count = {}
score = {}
for i in s:
    k = i.split()
    map[k[0]] = (int(k[3]), int(k[6]), int(k[13]))
    dist[k[0]] = 0
    score[k[0]] = 0
    fly_count[k[0]] = int(k[6])
    wait_count[k[0]] = int(k[13])
for i in range(2503):
    sec()
print('Part 1:', dist[winners()[0]])
print('Part 2:', score[sorted(score, key=score.get)[-1]])