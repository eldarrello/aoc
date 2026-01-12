import hashlib, re

def has3(s):
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
    salt = 'zpqevtbw'       #'abc'
    test = salt + str(i)
    for i in range(n):
        result = hashlib.md5(test.encode())
        test = str(result.hexdigest())
    return test

def eval(n):
    triples = {}
    found = 0
    for i in range(100000):
        hash = get_hash(i, n)
        c = has5(hash)
        if c:
            if c in triples:
                for ti in triples[c]:
                    if i - ti <= 1000:
                        found += 1
                        if found == 64:
                            break
                triples[c] = []
        t = has3(hash)
        if t:
            if t in triples:
                triples[t].append(i)
            else:
                triples[t] = [i]
        if found == 64:
            break
    return ti
print('Part 1:', eval(1))
print('Part 2:', eval(2017))


