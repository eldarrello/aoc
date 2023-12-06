def eval(time, d):
    return sum([1 for t in range(time) if (time - t) * t > d])
import math
t, d = open('input.txt').read().splitlines()
print("Part 1:", math.prod([eval(int(t), int(d.split()[1:][i])) for i, t in enumerate(t.split()[1:])]))
print("Part 2:", eval(int(''.join(t.split()[1:])), int(''.join(d.split()[1:]))))

'''
Just for fun I implemented the eval() based on formula too, even though to my disappointment
input data had low enough numbers to get result in seconds even with brute force.
#t^2 - time * t + distance > 0
def eval_fast(time, d):
    q = time / 2
    t2 = q + math.sqrt(q * q - d)
    t1 = q - math.sqrt(q * q - d)
    # time is discrete, thus need to floor and ceil
    return math.floor(t2) - math.ceil(t1) + 1
'''
