def eval(n):
    acc = 0
    for i in open('input.txt').read().split('\n\n'):
        x1, y1, x2, y2, x, y = map(int, i.replace('Button A: X+', '').replace('\nButton B: X+', ' ').replace('\nPrize: X=', ' ').replace(', Y+', ' ').replace(', Y=', ' ').split())
        x += n
        y += n
        t2 = (x1 * y - y1 * x) / (x1 * y2 - y1 * x2)
        t1 = (x - t2 * x2) / x1
        if int(t2) == t2 and int(t1) == t1:
            acc += 3 * int(t1) + int(t2)
    return acc
print("Part 1:", eval(0))
print("Part 2:", eval(10000000000000))

