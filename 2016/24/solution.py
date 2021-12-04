from itertools import combinations
from itertools import permutations

s = open('input.txt').read().splitlines()
h = len(s)
w = len(s[0])
map = []
for row in s:
    map += list(row)
all_keys = [x for x in map if x not in ['.', '#']]

def get_moves(p, visited):
    return [(p + d) for d in [w, -w, 1, -1] if (map[p + d] != '#') and p + d not in visited]

def get_move_count(start, end):
    visited = set()
    visited.add(start)
    moves = get_moves(start, visited)
    depth = 1
    while moves:
        new_moves = []
        while moves:
            p = moves.pop(0)
            if p == end:
                return depth
            if p in visited: continue
            visited.add(p)
            new_moves += get_moves(p, visited)
        moves = new_moves
        depth += 1
    return None

paths = list(combinations(all_keys, 2))
counts = {}
for path in paths:
    count = get_move_count(map.index(path[0]), map.index(path[1]))
    counts[path[0],path[1]] = count
    counts[path[1], path[0]] = count

k = [key for key in all_keys if key != '0']
key_sequence = list(permutations(k, len(k)))

def get_min_path(part_2):
    min_steps = 100000
    for sequence in key_sequence:
        if part_2:
            sequence += ('0',)
        prev_key = '0'
        total = 0
        for key in sequence:
            total += counts[prev_key, key]
            prev_key = key
        if total < min_steps:
            min_steps = total
    return min_steps

print("Part 1:", get_min_path(False))
print("Part 2:", get_min_path(True))
