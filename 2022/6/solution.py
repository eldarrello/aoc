def eval(part):
    s = open('input.txt').read()
    return [i for i in range(len(s) - part) if len(set(s[i:i + part])) == part][0] + part
print("Part 1:", eval(4))
print("Part 2:", eval(14))