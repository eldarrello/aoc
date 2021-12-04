s = open('input.txt').read().splitlines()


class Cart:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.turn = 0   # 0 - left, 1 - straight, 2 - right

    def __repr__(self):
        return "x={}, y={}".format(self.x, self.y)

    def get_pos(self):
        return self.y * 10000 + self.x

    def move(self):
        self.x += [-1, 0, 1, 0][self.direction]
        self.y += [0, -1, 0, 1][self.direction]
        v = s[self.y][self.x]
        if v == '+':
            if self.turn == 0:
                self.direction -= 1
            if self.turn == 2:
                self.direction += 1
            self.turn += 1
            self.turn %= 3
            self.direction %= 4
        if v == '\\':
            self.direction = [1, 0, 3, 2][self.direction]
        if v == '/':
            self.direction = [3, 2, 1, 0][self.direction]

carts = []
for y in range(len(s)):
    xs = [i for i, x in enumerate(s[y]) if x in '<>^v']
    if xs:
        for x in xs:
            d = s[y][x]
            carts.append(Cart(x, y, '<^>v'.index(d)))
    s[y] = s[y].replace('^', '|').replace('v', '|').replace('>', '-').replace('<', '-')

def move():
    carts.sort(key=lambda x: x.get_pos())
    #print(carts)
    for cart in carts:
        cart.move()
        pos = cart.get_pos()
        for c in carts:
            if c != cart and c.get_pos() == pos:
                carts.remove(cart)
                carts.remove(c)
                return pos % 10000, pos // 10000
    return None
for i in range(10000):
    t = move()
    if t:
        print("Part 1:", "{},{}".format(t[0], t[1]))
        break

for i in range(100000):
    t = move()
    if t and len(carts) == 1:
        pos = carts[0].get_pos()
        print("Part 2:", "{},{}".format(pos % 10000, pos // 10000))
        break

