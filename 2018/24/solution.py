import copy
class Group:
    def __init__(self, line, team):
        ws = line.split()
        self.units = int(ws[0])
        self.hitpoints = int(ws[4])
        self.initiative = int(ws[-1])
        self.damage = int(ws[-6])
        self.damage_type = ws[-5]
        self.immune_to = []
        self.weak_to = []
        self.team = team
        if ('(') in line:
            features = line.split('(')[1].split(')')[0].split('; ')
            for f in features:
                feature, ws = f.replace(',', '').split(' to ')
                if feature == 'immune':
                    self.immune_to = ws.split()
                elif feature == 'weak':
                    self.weak_to = ws.split()
    def get_attack_power(self):
        return self.units * self.damage
    def get_target_select_rank(self):
        return (self.get_attack_power(), self.initiative)
    def receive_attack_from(self, attacker):
        damage_factor = 1
        if attacker.damage_type in self.weak_to:
            damage_factor = 2
        full_units_eliminated = min(int(damage_factor * attacker.get_attack_power() / self.hitpoints), self.units)
        self.units -= full_units_eliminated
        return self.units == 0, full_units_eliminated

def get_team(lines, team):
    groups = []
    for line in lines.splitlines():
        if len(line) > 20:
            groups.append(Group(line, team))
    return groups

def get_attack_vector(a, targets):
    remaining_targets = list(targets)
    sorted_a = sorted([(g, g.get_target_select_rank()) for g in a], key=lambda x: x[1], reverse=True)
    attack_vector = []
    for i, _ in sorted_a:
        best_damage = 0
        selected_target = None
        for t in remaining_targets:
            damage = i.get_attack_power()
            if i.damage_type in t.immune_to:
                damage = 0
            elif i.damage_type in t.weak_to:
                damage *= 2
            if selected_target == None or damage > best_damage or (damage == best_damage and (t.get_attack_power() > selected_target.get_attack_power() or
                    (t.get_attack_power() == selected_target.get_attack_power() and t.initiative > selected_target.initiative))):
                best_damage = damage
                selected_target = t
        if selected_target and best_damage > 0:
            attack_vector.append((i.initiative, i, selected_target))
            remaining_targets.remove(selected_target)
    return attack_vector

def eval(a_, b_, extra_damage):
    a = copy.deepcopy(a_)
    for i in a:
        i.damage += extra_damage
    b = copy.deepcopy(b_)
    while a and b:
        total_units_lost = 0
        attack_vector = sorted(get_attack_vector(a, b) + get_attack_vector(b, a), reverse=True)
        for _, attacker, defender in attack_vector:
            if attacker in a or attacker in b:
                no_units_left, units_lost = defender.receive_attack_from(attacker)
                total_units_lost += units_lost
                if no_units_left:
                    if defender in a:
                        a.remove(defender)
                    elif defender in b:
                        b.remove(defender)
        if total_units_lost == 0:
            break
    return [sum(i.units for i in a), sum(i.units for i in b)]

s = open('input.txt').read()
a, b = s.split('\n\n')
a = get_team(a, 'immune system')
b = get_team(b, 'infection')

print("Part 1:", sum(eval(a, b, 0)))
for extra_damage in range(1, 10000, 1):
    result = eval(a, b, extra_damage)
    if result[0] > 0 and result[1] == 0:
        print("Part 2:", result[0])
        break

