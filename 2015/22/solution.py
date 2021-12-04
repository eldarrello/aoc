#damage, armor, heals, mana, cost in mana, turns
spells = {}
spells['Missile'] = [4, 0, 0, 0, 53, 0]
spells['Drain'] = [2, 0, 2, 0, 73, 0]
spells['Shield'] = [0, 7, 0, 0, 113, 6]
spells['Poison'] = [3, 0, 0, 0, 173, 6]
spells['Recharge'] = [0, 0, 0, 101, 229, 5]

def player_wins(seq, part_2):
    boss_score = 55
    boss_damage = 8
    player_score = 50
    player_mana = 500
    active_spells = {}
    turn = 0;
    total_cost = 0
    while len(seq):
        #print(player_mana)
        player_armor = 0
        #apply spells
        depleted_spells = []
        for i in active_spells:
            if i == 'Shield':
                player_armor = 7
            elif i == 'Poison':
                boss_score -= 3
            elif i == 'Recharge':
                player_mana += 101
            active_spells[i] -= 1
            if active_spells[i] == 0:
                depleted_spells.append(i)
        for i in depleted_spells:
            del active_spells[i]
        if turn % 2 == 0:
            # player turn
            if part_2:
                player_score -= 1
                if player_score <= 0:
                    return False
            spell = seq.pop(0)
            cost = spells[spell][4]
            player_mana -= cost
            total_cost += cost
            if player_mana < 0:
                return False
            if spells[spell][5] > 0:
                if spell in active_spells:
                    return -1
                active_spells[spell] = spells[spell][5]
            else:
                boss_score -= spells[spell][0]
                if boss_score <= 0:
                    return total_cost
                player_score += spells[spell][2]    #heal
        else:
            # boss turn
            player_score -= max(1, boss_damage - player_armor)
            if player_score <= 0:
                return False
        turn += 1
    return -1
seq_1 = ['Poison','Recharge', 'Shield', 'Poison', 'Missile',
       'Missile', 'Missile', 'Missile', 'Missile']
print('Part 1:', player_wins(seq_1, False))

seq_2 = ['Poison','Recharge', 'Shield', 'Poison', 'Recharge', 'Drain', 'Poison',
       'Drain', 'Missile']
print('Part 2:', player_wins(seq_2, True))
#todo::find best sequences programmatically. So far the sequeces were tuned manually