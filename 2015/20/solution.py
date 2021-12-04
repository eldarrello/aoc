#Taken from reddit. Myself did only part 1, while part 2 was too slow without the neat optimization to use small divisors for finding large divisors
import math

def divisors(n):
    small_divisors = [i for i in range(1, int(math.sqrt(n)) + 1) if n % i == 0]
    large_divisors = [n / d for d in small_divisors if n != d * d]
    return small_divisors + large_divisors

target = 33100000
part_one, part_two = None, None
i = 0
while not part_one or not part_two:
    i += 1
    ds = divisors(i)
    if not part_one:
        if sum(ds) * 10 >= target:
            part_one = i
    if not part_two:
        if sum(d for d in ds if i / d <= 50) * 11 >= target:
            part_two = i
print('Part 1:', part_one)
print('Part 2:', part_two)

'''
#Annother really simple one from reddit:

from collections import defaultdict

target = 33100000

def part1(upperBound):
    houses = defaultdict(int)

    for elf in range(1, target):
        for house in range(elf, upperBound, elf):
            houses[house] += elf * 10

        if houses[elf] >= target:
            return elf

def part2(upperBound):
    houses = defaultdict(int)

    for elf in range(1, target):
        for house in range(elf, min(elf * 50 + 1, upperBound), elf):
            houses[house] += elf * 11

        if houses[elf] >= target:
            return elf

print(part1(1000000))
print(part2(1000000))

'''