s = open('input.txt').read().splitlines()
s = [int(x) for x in s]

def part1():
    for i in s:
        for j in s:
            if i != j and i + j == 2020:
                print("Part 1:", i * j)
                return

def part2():
    for i in s:
        for j in s:
            for l in s:
                if i != j and j != l and i + j + l == 2020:
                    print("Part 2:", i * j * l)
                    return

part1()
part2()