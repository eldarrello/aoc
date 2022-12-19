def eval(bp, n):
    max_score = 0
    min_time = n
    nodes = [([1, 0, 0, 0], [0, 0, 0, 0], 0)]
    while nodes:
        robots, resources, time = nodes.pop()
        if robots[3] == 0 and time > min_time:
            continue
        if time == n:
            if resources[-1] > max_score:
                max_score = resources[-1]
            continue
        can_build = []
        for i in range(4):
            for j in range(3):
                if resources[j] < bp[i][j]:
                    break
            else:
                can_build.append(i)
        if 3 in can_build and time < min_time:
            min_time = time
        if len(can_build) > 1:
            if can_build[-1] > 1:
                can_build = [can_build[-1]]
        resources = [resources[i] + robots[i] for i in range(4)]
        if can_build:
            for i in can_build:
                new_robots = list(robots)
                new_robots[i] += 1
                new_resources = list(resources)
                for j in range(3):
                    new_resources[j] -= bp[i][j]
                nodes.append((new_robots, new_resources, time + 1))
            if len(can_build) == 1 and (can_build[0] in [1, 2]):
                nodes.append((robots, resources, time + 1))         # Reducing no build steps is most important!
        else:
            nodes.append((robots, resources, time + 1))
    return max_score
bps = []
for i in open('input.txt').read().splitlines():
    t = i.split()
    bps.append(([int(t[6]), 0, 0], [int(t[12]), 0, 0], [int(t[18]), int(t[21]), 0], [int(t[27]), 0, int(t[30])]))
print("Part 1:", sum([(i + 1) * eval(bps[i], 24) for i in range(len(bps))]))
print("Part 2:", eval(bps[0], 32) * eval(bps[1], 32) * eval(bps[2], 32))
