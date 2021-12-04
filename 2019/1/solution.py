total_fuel = 0
with open('input.txt') as fp:
    for line in fp:
        mass = int(line)
        while mass > 6:
            mass = mass / 3 - 2
            total_fuel += mass
print(total_fuel)