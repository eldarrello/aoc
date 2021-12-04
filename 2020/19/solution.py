s = open('input.txt').read().splitlines()
rules = {i.split(': ')[0]:[[t.strip('"') for t in j.split()] for j in i.split(': ')[1].split(' | ')] for i in s if ': ' in i}
base = {}
def solve(k):
    solved = set()
    for rs in rules[k]:
        h = []
        for r in rs:
            if r in ["a", "b"]:
                base[k] = r
                return
            if r not in base:
                return
            h = [x + y for x in h for y in base[r]] if h else base[r]
        solved = solved.union(set(h))
    base[k] = solved
def valid2(m, n, a ,b):
    for i in [m[i:i + n] for i in range(0, len(m), n)]:
        a += 1 if b == 0 and i in base['42'] else 0
        b += 1 if a > 0 and i in base['31'] else 0
    return b > 0 and a > b and a + b == len(m) // n
[[solve(k) for k in rules.keys() if k not in base] for i in range(len(rules) **2)]
print("Part 1:", sum(i in base['0'] for i in s if ':' not in i))
print("Part 2:", sum(valid2(i, 8, 0, 0) for i in s if ':' not in i))