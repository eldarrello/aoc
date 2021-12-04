s = open('input.txt').read().splitlines()
f = ''
count_1 = 0
count_2 = 0
s += ['']
for i in s:
    if i == "":
        r = [x.split(":")[0] for x in f.split()]
        n = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
        for k in n:
            if k not in r: break
        else:
            count_1 += 1
            for a in f.split():
                k, v = a.split(":")
                if k == "byr" and int(v) >= 1920 and int(v) <= 2002:continue
                if k == "iyr" and int(v) >= 2010 and int(v) <= 2020: continue
                if k == "eyr" and int(v) >= 2020 and int(v) <= 2030: continue
                if k == "hgt" and v[-2:] in ['cm', 'in']:
                    if v[:-2].isnumeric():
                        vv = int(v[:-2])
                        if v[-2:] == "cm" and vv >= 150 and vv <= 193: continue
                        if v[-2:] == "in" and vv >= 59 and vv <= 76: continue
                if k == "hcl" and len(v) == 7 and v[0] == '#':
                    for b in v[1:]:
                        if not (b in range(ord('0'), ord('9') + 1) or b in range(ord('a'), ord('f') + 1)):
                            break
                    continue
                if k == "ecl" and v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']: continue
                if k == "pid" and len(v) == 9 and v.isnumeric(): continue
                if k == "cid": continue
                break
            else:
                count_2 += 1
        f = ''
    else:
        f += " " + i
print("Part 1:", count_1)
print("Part 2:", count_2)