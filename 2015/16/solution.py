s = open('input.txt').read().splitlines()
d = {
"children": 3,
"cats": 7,
"samoyeds": 2,
"pomeranians": 3,
"akitas": 0,
"vizslas": 0,
"goldfish": 5,
"trees": 3,
"cars": 2,
"perfumes": 1
}

def match(i, part_2):
    k = i.replace(':', '').replace(',', '').split(' ')[2:]
    for key in d:
        if key in k:
            if part_2 and key in ['cats', 'trees']:
                if d[key] >= int(k[k.index(key) + 1]):
                    return False
            elif part_2 and key in ['pomeranians', 'goldfish']:
                if d[key] <= int(k[k.index(key) + 1]):
                    return False
            else:
                if d[key] != int(k[k.index(key) + 1]):
                    return False

    return True

for i in s:
    if match(i, False):
        print('Part 1:', s.index(i) + 1)
    if match(i, True):
        print('Part 2:', s.index(i) + 1)


