s = open('input.txt').read().splitlines()
scores = [{} for x in range(len(s[1]))]
for i in s:
    for k in range(len(scores)):
        if list(i)[k] in scores[k]:
            scores[k][list(i)[k]] += 1
        else:
            scores[k][list(i)[k]] = 1
message_1 = []
message_2 = []
for k in range(len(scores)):
    x = sorted(scores[k].items(), key=lambda item: item[1], reverse = True)
    message_1.append(x[0][0])
    message_2.append(x[-1][0])
print('Part 1:', ''.join(message_1))
print('Part 2:', ''.join(message_2))
