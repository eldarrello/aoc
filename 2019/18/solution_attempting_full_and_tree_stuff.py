file = "input_0.txt"
s = open(file).read().splitlines()
w = len(s[0])
h = len(s)
map = []
for y in range(h):
 for a in s[y]:
     map.append(a)

all_keys = ['@']
for a in map:
    if ord(a) in range(ord('a'), ord('z') + 1):
        all_keys.append(a)
all_keys.sort()
#print('all_keys', ''.join(all_keys))

def in_path(p, path):
    for i in path:
        if p == i[2]:
            return True
    return False

def get_path(p, key):
    if map[p] == key:
        return []
    print(map[p], key)
    moves = [-w, w, 1, -1]
    commands = [0, 1, 2, 3]
    path = []
    best_path = []
    p0 = p
    while len(commands):
        c = commands.pop()
        v = map[p + moves[c]]
        if v == '#': continue
        x = p + moves[c]
        if len(commands) and in_path(x, path): continue
        if len(commands) and x == p0: continue
        if v == key:
            if len(path) + 1 < len(best_path) or len(best_path) == 0:
                best_path = path.copy() + [(commands, v, x)]
            continue
        if len(path) > len(best_path) and len(best_path) > 0:
            continue
        p = x
        if len(commands) or len(path) == 0:
            path.append((commands, v, p))
            commands = [c ^ 1 + x for x in [0, 1, 2, -1]]
        else:
            commands, v, x = path.pop()
    return best_path

def get_moves(keys, steps):
    base_key = keys[-1]
    moves = []
    keys_to_get = []
    for key in all_keys:
        if key not in keys:
            keys_to_get.append(key)
    for key in keys_to_get:
        n, req_keys, gets_keys = lookup[(base_key, key)]
        if all(elem in keys for elem in req_keys):
            keys_after_move = keys.copy()
            for i in gets_keys:
                if i not in keys_after_move:
                    keys_after_move.append(i)
            move = (keys_after_move, steps + n)
            moves.append(move)
    #moves.sort(key=lambda m: m[1])
    return moves

def get_hash(keys):
    ks = keys.copy()
    if len(keys) == len(all_keys):
        ks.sort()
    elif len(keys) > 1:
        last = ks[-1]
        ks.remove(last)
        ks.sort()
        ks.append(last)
    return ''.join(ks)

all_hash = get_hash(all_keys)

def get_score(move):
    steps = move[1]
    #moves = get_moves(move[0], move[1])
    #for i in moves:
    #    steps += i[1]
    return steps

def full_eval(keys):
    seq = []
    steps = 0
    moves = get_moves(keys, steps)
    mins = {}
    while True:
        move = moves.pop(0)
        #make move
        keys = move[0]
        steps = move[1]
        score = get_score(move)
        hash = get_hash(keys)
        if hash in mins:
            if score < mins[hash]:
                mins[hash] = score
                if hash == all_hash:
                    print(steps, keys)
            else:
                if len(moves) > 0:
                    continue
                if len(seq) == 0:
                    break
                moves = seq.pop()
                continue
                t = 9
        else:
            mins[hash] = score

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
            moves = get_moves(keys, steps)
    return mins
'''
class Node:
    def __init__(self, parent, steps, value):
        self.parent = parent
        self.childs = []
        self.steps = steps
        self.value = value

def add_child(node, steps, value):
    n = Node(node, steps, value)
    node.childs.append(n)
    return n

def get_tree(p):
    moves = [-w, w, 1, -1]
    commands = [0, 1, 2, 3]
    path = []   #for traversing not to pollute tree with commands, which are later not needed
    node = Node(None, 0, '@')
    while len(commands):
        c = commands.pop()
        if map[p + moves[c]] == '#': continue
        p += moves[c]
        if len(commands) or len(path) == 0:
            path.append(commands)
            node = add_child(node, 1, map[p])
            commands = [c ^ 1 + x for x in [0, 1, 2, -1]]
        else:
            commands = path.pop()
            #Reduce dead-ends without any keys
            if len(node.childs) == 0 and not node.value.islower():
                node.parent.childs.remove(node)
            #Reduce empty paths. Keep only empty junctions to be able to count steps.
            if len(node.childs) == 1 and node.value == '.':
                node.childs[0].steps += node.steps
                node.childs[0].parent = node.parent
                node.parent.childs.append(node.childs[0])
                node.parent.childs.remove(node)
            node = node.parent
    return node

def traverse(node):
    doors = [node.value] if node.value.isupper() else []
    keys = [node.value] if node.value.islower() else []
    leafs = [node.value] if len(node.childs) == 0 else []
    nodes = 1
    for n in node.childs:
        n, l, d, k = traverse(n)
        nodes += n
        leafs +=l
        doors += d
        keys  += k
    return nodes, leafs, doors, keys

def find_node(node, key):
    if node.value == key:
        return node
    for n in node.childs:
        x = find_node(n, key)
        if x != None:
            return x
    return None

def get_distance_and_doors(key, key2):
    node = find_node(root, key)
    node2 = find_node(root, key2)
'''
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
            l = len(path)
            if transit(key, key2) or transit(key2, key):
                l -= 2
            lookup[(key, key2)] = (l, needed_keys, gets_keys)
    return lookup

lookup = get_lookup()
for k, v in lookup.items():
    print(k, v)
print('total keys:', len(all_keys))
mins = full_eval(['@'])
print(len(mins), mins[get_hash(all_keys)])
#root = get_tree(o)
#print(traverse(root))


#idea is to create key to key map with distances as number of steps
#then evaluate minimal number of steps by set of keys

#5678
#5128
#5012
#4918
#4872
#4022
#4878

4872 ['@', 'h', 'w', 'a', 'j', 'x', 'p', 'z', 'i', 't', 'v', 'e', 'g', 'r', 'c', 'n', 'l', 'y', 'f', 'm', 'u', 'b', 'q', 'o', 'd', 's', 'k']