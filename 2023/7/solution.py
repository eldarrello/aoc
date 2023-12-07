def get_hand_rank(h):
    return sum([h.count(i) * h.count(i) for i in h])

def eval(h, swap, card_rank):
    return max([get_hand_rank(h.replace(swap, x)) for x in h]) * 16 ** 6 + sum([16 ** (5 - i) * card_rank.index(v) for i, v in enumerate(h)])

hands = [(i.split()) for i in open('input.txt').read().splitlines()]
print("Part 1:", sum([int(bid) * (i + 1) for i, (hand, bid) in enumerate(sorted(hands, key = lambda x: eval(x[0], '', '23456789TJQKA')))]))
print("Part 2:", sum([int(bid) * (i + 1) for i, (hand, bid) in enumerate(sorted(hands, key = lambda x: eval(x[0], 'J', 'J23456789TQKA')))]))

