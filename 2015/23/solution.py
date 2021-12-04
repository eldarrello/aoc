s = open('input.txt').read().splitlines()

def run(a):
    r = {'a': a, 'b': 0}
    ip = 0
    while ip < len(s):
        ss = s[ip].split(' ')
        if ss[0] == 'hlf':
            r[ss[1]] /= 2
            ip += 1
        if ss[0] == 'tpl':
            r[ss[1]] *= 3
            ip += 1
        if ss[0] == 'inc':
            r[ss[1]] += 1
            ip += 1
        if ss[0] == 'jmp':
            ip += int(ss[1])
        if ss[0] == 'jie':
            ip += int(ss[2]) if r[ss[1][:1]] % 2 == 0 else 1
        if ss[0] == 'jio':
            ip += int(ss[2]) if r[ss[1][:1]] == 1 else 1
    return r['b']

print('Part 1:', run(0))
print('Part 2:', run(1))
