class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Circle:
    def __init__(self):
        self.head = None
        self.n = 0

    def insert(self, new_data):
        new_node = Node(new_data)
        if self.head == None:
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
        else:
            node = self.head.next
            new_node.prev = node
            new_node.next = node.next
            node.next.prev = new_node
            node.next = new_node
            self.head = new_node
        self.n += 1

    def remove(self):
        node = self.head
        for i in range(7):
            node = node.prev
        node.prev.next = node.next
        node.next.prev = node.prev
        self.head = node.next
        self.n -= 1
        return node.data

    def printList(self):
        print('---')
        item = self.head
        for i in range(self.n):
            print(item.data, item.prev.data, item.next.data)
            item = item.next

def play(players, n):
    circle = Circle()
    circle.insert(0)
    points = {}
    for i in range(1, n + 1):
        if i % 23 == 0:
            player = i % players
            if player not in points:
                points[player] = 0
            points[player] += circle.remove() + i
        else:
            circle.insert(i)
    return max(points.values())
print("Part 1:", play(448, 71628))
print("Part 2:", play(448, 71628 * 100))

