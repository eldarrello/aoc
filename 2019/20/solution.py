file = "input.txt"
s = open(file).read().splitlines()
h = len(s)
w = len(s[0])
map = []
for y in range(h):
    for a in s[y]:
        map.append(a)

def get_destination(id, p):
    for i in range(len(map) - w):
        if i == p or i + 1 == p or i + w == p: continue
        [y, x] = divmod(i, w)
        if map[i] == id[0] and  x != w - 1 and x != 1:
            outer = True if x < 2 or x > w - 3 or y < 2 or y > h - 3 else False
            if map[i + w] == id[1]:
                if map[i - w] == '.':
                    return i - w, 0, outer
                else:
                    return i + 2 * w, 1, outer
            elif map[i + 1] == id[1]:
                if map[i + 2] == '.':
                    return i + 2, 2, outer
                else:
                    return i - 1, 3, outer
    return 0, 0, 0

def has_move(path, p, level):
    for move in path:
        if move[1] == (p, level):
            return True
    return False

def get_commands(c) :
    return [c ^ 1 + x for x in [0, 1, 2, -1]]

def get_steps(p, c, level, part_2):
    moves = [-w, w, 1, -1]
    commands = get_commands(c)
    path = []
    min_path = 10000
    portals = ['AA']
    prev_portal = 'AA'
    while len(commands):
        c = commands.pop()
        if has_move(path, p + moves[c], level) and len(commands) > 0:
            #print('loop @', p + moves[c] )
            continue
        v = map[p + moves[c]]
        if v == '#': continue
        if v == '.':
            p += moves[c]
        else:
            portal = v + map[p + 2 * moves[c]] if moves[c] > 0 else map[p + 2 * moves[c]] + v
            if portal == 'AA':
                if level == 0:
                    return min_path
                else: continue
            if portal == 'ZZ':
                if level == 0 and len(path) < min_path:
                    min_path = len(path)
                    if part_2: break
                    #print(min_path)
                continue
            new_p, c, outter = get_destination(portal, p + moves[c])
            if part_2:
                if level == 0 and outter == False: continue
                if outter:
                    if portal in portals and len(commands) > 0:
                        #print('skip', portal)
                        continue
                    level += 1
                    portals.append(portal)
                else:
                    level -= 1
                    portals.pop()
            p = new_p
            #print(prev_portal, '->', portal, '@', level, 'steps:', len(path))
            prev_portal = portal
        if len(commands):
            path.append((commands, (p, level)))
            commands = get_commands(c)
        else:
            commands, q = path.pop() #currently q gets discarded but instead of back move we could restore p directly from stack
    return min_path

#todo: do not hard code direction(2)
p, c, outer = get_destination('AA', 2)
print('Part 1 number of steps:', get_steps(p, c, 0, False))
#todo make part_2 faster and search for best path or maybe there is only single path?
print('Part 2 number of steps:', get_steps(p, c, 0, True))
