import hashlib
import re

def getFirst3(s):
    m = re.findall(r"(\w)\1{2,}", s)
    if len(m) > 0:
        return m[0]
    return None

def has5(s):
    m = re.findall(r"(\w)\1{4,}", s)
    if len(m) > 0:
        return m[0]
    return None

def get_hash(i, n):
    #salt = 'abc'
    salt = 'qzyelonm'
    test = salt + str(i)
    for i in range(n):
        result = hashlib.md5(test.encode())
        test = str(result.hexdigest())
    return test

#todo::it has a bug that it doesn't work for part 1 (result is one key off)
def part_2():
    c = {}
    found = 0
    for i in range(25000):
        s = get_hash(i, 2017)
        k = getFirst3(s)
        if k:
            if k in c:
                c[k].append(1000)
            else:
                c[k] = [1000]
        k = has5(s)
        if k:
            if k not in c: continue
            for t in c[k]:
                if t < 1000:
                    found += 1
                    if found == 64:
                        print('Part 2:', i - (1000 - t))
                        return
            c[k] = [1000]
        for k in c:
            for j in range(len(c[k])):
                c[k][j] -= 1
            if 0 in c[k]:
                c[k].remove(0)

def part_1():
    found = 0
    for i in range(17000):
        s = get_hash(i, 1)
        k = getFirst3(s)
        if not k: continue
        for j in range(i + 1, i + 1000 + 1):
            s = get_hash(j, 1)
            p = has5(s)
            if p and k == p:
                found += 1
                if found == 64:
                    print('Part 1:', i)
part_1()
part_2()

