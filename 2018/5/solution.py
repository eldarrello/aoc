s = open('input.txt').read()
def run(a):
    p = []
    for i in s:
        o = ord(i)
        if o != a and o != a | 0x20:
            if p and o ^ 0x20 == p[-1]:
                p.pop()
            else:
                p.append(o)
    return len(p)
print("Part 1: ", run(ord(' ')))
print("Part 2: ", min(run(i) for i in range(ord('A'), ord('Z') + 1)))