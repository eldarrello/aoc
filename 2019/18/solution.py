file = "input.txt"
s = open(file).read().splitlines()
w = len(s[0])
h = len(s)

def get_path(p, key):
    if map[p] == key:
        return []
    moves = [-w, w, 1, -1]
    commands = [0, 1, 2, 3]
    path = []
    while len(commands):
        c = commands.pop()
        v = map[p + moves[c]]
        if v == '#': continue
        p = p + moves[c]
        if v == key:
            return path.copy() + [(commands, v, p)]
        if len(commands) or len(path) == 0:
            path.append((commands, v, p))
            commands = [c ^ 1 + x for x in [0, 1, 2, -1]]
        else:
            commands, v, x = path.pop()
    return path

def get_lookup():
    lookup = {}
    for key in all_keys:
        p = map.index(key)
        for key2 in all_keys:
            path = get_path(p, key2)
            needed_keys = []
            gets_keys = []
            for m in path:
                v = m[1]
                if v.isupper():
                    needed_keys.append(v.lower())
                elif v.islower():
                    gets_keys.append(v)
            lookup[(key, key2)] = (len(path), needed_keys, gets_keys)
    return lookup

def get_moves(state, keys, steps):
    moves = []
    keys_to_get = []
    for key in all_keys:
        if key not in keys:
            keys_to_get.append(key)
    for key in keys_to_get:
        for q in range(len(state)):
            n, req_keys, gets_keys = lookup[(state[q], key)]
            if n > 0 and all(elem in keys for elem in req_keys):
                keys_after_move = keys.copy()
                for i in gets_keys:
                    if i not in keys_after_move:
                        keys_after_move.append(i)
                new_state = state.copy()
                new_state[q] = key
                move = (keys_after_move, steps + n, new_state)
                moves.append(move)
    return moves

def evaluate(state):
    seq = []
    steps = 0
    keys = state
    moves = get_moves(state, keys, steps)
    mins = {}
    while True:
        move = moves.pop(0)
        #make move
        keys = move[0]
        steps = move[1]
        state = move[2]
        keys.sort()
        hash = ''.join(keys)
        if len(keys) < len(all_keys):
              hash += ''.join(state)
        if hash in mins:
            if steps < mins[hash]:
                mins[hash] = steps
            else:
                if len(moves) > 0:
                    continue
                if len(seq) == 0:
                    break
                moves = seq.pop()
                continue
        else:
            mins[hash] = steps
        #End condition
        if len(keys) == len(all_keys):
            if len(moves) > 0:
                continue
            if len(seq) == 0:
                break
            moves = seq.pop()
        else:
            if len(moves):
                seq.append(moves)
            moves = get_moves(state, keys, steps)
    return mins

def transit(key1, key2):
    p0 = map.index('@')
    p0_x = p0 % w
    p1 = map.index(key1)
    p1_x = p1 % w
    p2 = map.index(key2)
    p2_x = p2 % w
    if p1 < p0 and p2 > p0:
        if (p1_x < p0_x and p2_x < p0_x) or (p1_x > p0_x and p2_x > p0_x):
            return True
    return False

def get_map():
    map = []
    for y in range(h):
        for a in s[y]:
            map.append(a)
    return map

def get_all_keys(state):
    all_keys = state.copy()
    for a in map:
        if ord(a) in range(ord('a'), ord('z') + 1):
            all_keys.append(a)
    all_keys.sort()
    return all_keys

#part_1
map = get_map()
o = map.index('@')
map[o - 1] = '#'            #close open space
map[o + 1] = '#'
state = ['@']
all_keys = get_all_keys(state)
lookup = get_lookup()
for k, v in lookup.items():
    if transit(k[0], k[1]) or transit(k[1], k[0]):
        lookup[k] = (v[0] - 2, v[1], v[2])  #compensate for closing space
mins = evaluate(state)
print('Part 1:', mins[''.join(all_keys)])

#part_2
map = get_map()
o = map.index('@')
map[o - 1] = '#'
map[o + 1] = '#'
map[o + w] = '#'
map[o - w] = '#'
start_pos = [o - w - 1, o - w + 1, o + w - 1, o + w + 1]
state = ['1', '2', '3', '4']
all_keys = get_all_keys(state)
for q in range(len(state)):
    map[start_pos[q]] = state[q]
lookup = get_lookup()
mins = evaluate(state)
print('Part 2:', mins[''.join(all_keys)])

#todo:keys as bitfields, open area search without hack