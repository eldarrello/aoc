m = [1] + sum([[0, int(i.split()[1])] if 'addx' in i else [0] for i in open('input.txt').read().splitlines()], [])
print("Part 1:", sum([i * sum(m[:i]) for i in range(20, 221, 40)]))
print('\n'.join([''.join(['#' if sum(m[:y * 40 + x + 1]) in [x - 1, x, x + 1] else ' ' for x in range(40)]) for y in range(6)]))
