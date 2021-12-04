s = open('input.txt').read().splitlines()
s = [int(x) for x in s]
part_1 = 0
for i in range(1, len(s)):
    if s[i] > s[i - 1]:
        part_1 += 1

part_2 = 0
prev_sum = 0
for i in range(len(s) - 2):
    sum = s[i] + s[i + 1] + s[i + 2]
    if sum > prev_sum and prev_sum != 0:
        part_2 += 1
    prev_sum = sum
print("Part 1:", part_1)
print("Part 2:", part_2)