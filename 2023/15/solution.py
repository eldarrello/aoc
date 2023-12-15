boxes = [{} for i in range(256)]
for k in open('input.txt').read().split(','):
    hashes = [v:= 17 * ((v if i else 0) + ord(c)) % 256 for i, c in enumerate(k)]
    acc1 = hashes[-1] + (acc1 if 'acc1' in vars() else 0)
    label = ''.join([c for c in k if c.isalpha()])
    h = hashes[len(label) - 1]
    if '-' in k:
        boxes[h].pop(label, "")
    else:
        boxes[h][label] = int(k[-1])
print("Part 1:", acc1)
print("Part 2:", sum([(i + 1) * (k + 1) * f for i, box in enumerate(boxes) for k, f in enumerate(box.values())]))

