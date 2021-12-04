import math

with open("input.txt") as fp: map = fp.read().replace('\n','')
   
def yx(i):
    return divmod(i, math.sqrt(len(map)))

def get_visible(s):
    d = {}
    for i in [i for i, c in enumerate(map) if c == '#' and i != s]:
        dx = yx(i)[1] - yx(s)[1]
        dy = yx(i)[0] - yx(s)[0]
        angle = math.atan2(-dx, dy)
        distance = dy * dy + dx * dx
        if angle in d and distance >= d[angle][0]: continue
        d[angle] = [distance, int(100 * yx(i)[1] + yx(i)[0])]
    return [len(d), sorted(d.items())]

station = max([[get_visible(i), i] for i, c in enumerate(map) if c == '#'])
print('max visible asteroids', station[0][0], '@', yx(station[1]), '@200:', station[0][1][199][1][1])