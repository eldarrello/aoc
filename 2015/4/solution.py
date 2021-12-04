s = open('input.txt').read()

import hashlib
got_part_1 = False
for i in range(10000000):
    k = s + str(i)
    result = hashlib.md5(k.encode())
    if result.hexdigest()[0:5] == "00000" and got_part_1 == False:
        print('Part 1:', i)
        got_part_1 = True
    if result.hexdigest()[0:6] == "000000":
        print('Part 2:', i)
        break