def run(part):
    s = open('input.txt').read().splitlines()
    m = {}
    for i in s:
        ws = i.split()
        a = ws[1]
        b = ws[7]
        m[b] = m[b] + [a] if b in m else [a]
        if a not in m:
            m[a] = []
    seq = []
    in_progress = {}
    acc = 0
    while m:
        a = [k for k, v in m.items() if not v]
        if part == 1:
            a.sort()
            seq.append(a[0])
            done = [a[0]]
        else:
            while a and len(in_progress) < 5:
                t = a.pop(0)
                if t not in in_progress:
                    in_progress[t] = 61 + ord(t) - ord('A')
            done = []
            while not done:
                for k, v in in_progress.items():
                    in_progress[k] -= 1
                    if in_progress[k] == 0:
                        done.append(k)
                acc += 1
        for i in done:
            if i in in_progress:
                del in_progress[i]
            del m[i]
            for k, v in m.items():
                if i in v:
                    m[k].remove(i)
    return ''.join(seq), acc
print("Part 1:", run(1)[0])
print("Part 2:", run(2)[1])