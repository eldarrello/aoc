s = open('input.txt').read().splitlines()
for i in s:
    r = [x.strip() for x in i.split(' ') if x != '']
    #print(r)
#boss

def player_wins(b_d, b_a):
    print(b_d, b_a)
    # boss
    a = 104
    a_d = 8
    a_a = 1
    # player
    b = 100
    da = max(1, b_d - a_a)
    db = max(1, a_d - b_a)
    return True if a // da <= b // db else False

import random
while True:
    print(player_wins(random.randrange(4, 10), random.randrange(1, 10)))
print('Part 1:', 78) #damage 8, armor 1

print('Part 2:', 148) #damage 7, armor 1

#todo::auto resolve