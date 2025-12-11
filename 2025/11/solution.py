def cp(cache, node):
    if node not in cache:
        cache[node] = sum([cp(cache, i) for i in (m[node] if node in m else [])])
    return cache[node]
s = open('input.txt').read().splitlines()
m = {l.split(':')[0]: l.split(':')[1].split() for l in s}
print("Part 1:", cp({'out': 1}, 'you'))
print("Part 2:", cp({'fft': 1}, 'svr') * cp({'dac': 1}, 'fft') * cp({'out': 1}, 'dac'))
