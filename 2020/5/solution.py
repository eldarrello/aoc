ids = [int(i.replace('F', '0').replace('B', '1').replace('R', '1').replace('L', '0'), 2) for i in open('input.txt').read().splitlines()]
print("Part 1:{}\nPart 2:{}".format(max(ids), [id for id in range(min(ids), max(ids)) if id not in ids][0]))



