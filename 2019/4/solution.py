def validate_1(y):
    x = []
    has_pair = False
    for ch in str(y):
        x.append(int(ch))
    for i in range(5):
        if x[i] > x[i + 1]:
            return False
        elif x[i] == x[i + 1]:
            has_pair = True
    return has_pair
    
def validate_2(y):
    x = []
    has_pair = False
    for ch in str(y):
        x.append(int(ch))
    for i in range(5):
        if x[i] > x[i + 1]:
            return False
        elif x[i] == x[i + 1]:
            if i > 0 and x[i - 1] == x[i]:
                continue
            elif i < 4 and x[i + 2] == x[i]:
                continue
            has_pair = True
    return has_pair
    
c = 0
i = 158126
while i < 624574:
    if (validate_2(i)):
        c += 1;
    if i % 100000 == 0:
        print('*')
    i += 1
print c
