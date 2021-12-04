import itertools
import copy

s = open('input.txt').read().splitlines()

def load_items(s):
    items = {}
    for i in range(4):              #number of floors
        words = s[i].split(' ')
        for k in range(len(words)):
            word = words[k]
            if '-' in word:
                key = word.split('-')[0]
                key = key[:2].upper() + 'M'
                items[key] = i + 1
            elif 'generator' in word:
                key = (words[k - 1])
                key = key[:2].upper() + 'G'
                items[key] = i + 1
    items['E'] = 1
    return items

def check_fry(floor):
    gs = []
    ms = []
    for i in floor:
        type = i[-1:]
        name = i[:-1]
        if type == 'G':
            gs.append(name)
        else:
            ms.append(name)
    if not gs: return False
    for i in ms:
        if i not in gs:
            return True

def get_floor(d, floor):
    items = []
    for i in d.items():
        if i[1] == floor and i[0] != 'E':
            items.append(i[0])
    return items

def get_moves(items, states):
    moves = []
    source_floor = items['E']
    items_s = get_floor(items, source_floor)
    try_moves = items_s + list(itertools.combinations(items_s, 2))
    destination_floors = [[], [2], [1, 3], [2, 4], [3]]
    for destination_floor in destination_floors[source_floor]:
        for i in try_moves:
            mm = copy.deepcopy(items)
            if type(i) is tuple:
                for k in i:
                    mm[k] = destination_floor
            else:
                mm[i] = destination_floor
            if not check_fry(get_floor(mm, source_floor)) and not check_fry(get_floor(mm, destination_floor)):
                mm['E'] = destination_floor
                fz = frozenset(mm.items())
                if fz not in states:
                    states.add(fz)
                    moves.append(mm)
    return moves

def solve(items):
    states = set()
    #elevator starts from 1. floor and all items need to be taken to 4. floor. Microchips without power will be fried by other generators
    moves = get_moves(items, states)
    level = 1
    while moves:
        next_moves = []
        while moves:
            items = moves.pop(0)
            tt = list(items.values())
            if tt[1:] == tt[:-1] and tt[0] == 4:
                return level
            next_moves += get_moves(items, states)
        moves = next_moves
        #print(level, len(moves))
        level += 1
    return -1

part_1_result = solve(load_items(s))
print("Part 1:", part_1_result)
s[0] += ' An elerium generator. An elerium-compatible microchip.'# A dilithium generator. A dilithium-compatible microchip.'
part_1_and_one_extra_pair = solve(load_items(s))
print("Part 2:", part_1_result + 2 * (part_1_and_one_extra_pair - part_1_result)) #adding 2 pairs makes it too slow and would need to make the search smarter. Instead we cheat a bit
