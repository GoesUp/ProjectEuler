from collections import Counter

cards = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}


def royal_flush(cards1, cards2):
    colors1, colors2 = [i[1] for i in cards1], [i[1] for i in cards2]
    values1, values2 = [i[0] for i in cards1], [i[0] for i in cards2]
    colors1, colors2 = list(set(colors1)), list(set(colors2))
    values1, values2 = list(set(values1)), list(set(values2))
    if len(colors1) == 1 and all([True if a in values1 else False for a in ["T", "J", "Q", "K", "A"]]):
        return 1
    if len(colors2) == 1 and all([True if a in values2 else False for a in ["T", "J", "Q", "K", "A"]]):
        return -1
    return 0


def straight_flush(cards1, cards2):
    colors1, colors2 = [i[1] for i in cards1], [i[1] for i in cards2]
    values1, values2 = [cards[i[0]] for i in cards1], [cards[i[0]] for i in cards2]
    colors1, colors2 = list(set(colors1)), list(set(colors2))
    values1, values2 = sorted(list(set(values1))), sorted(list(set(values2)))
    if len(colors1) == 1 and len(values1) == 5 and values1[-1] - values1[0] == 4:
        if len(colors2) == 1 and len(values2) == 5 and values2[-1] - values2[0] == 4:
            if sum(values1) > sum(values2):
                return 1
            else:
                return -1
        else:
            return 1
    elif len(colors2) == 1 and len(values2) == 5 and values2[-1] - values2[0] == 4:
        return -1
    return 0


def four_of_a_kind(cards1, cards2):
    values1, values2 = [cards[i[0]] for i in cards1], [cards[i[0]] for i in cards2]
    values1, values2 = dict(Counter(values1)), dict(Counter(values2))
    if max(values1.values()) == 4:
        if max(values2.values()) == 4:
            if max(values1, key=values1.get) > max(values2, key=values2.get):
                return 1
            elif max(values1, key=values1.get) < max(values2, key=values2.get):
                return -1
            else:
                return high_card(cards1, cards2)
        else:
            return 1
    elif max(values2.values()) == 4:
        return -1
    return 0


def full_house(cards1, cards2):
    values1, values2 = [cards[i[0]] for i in cards1], [cards[i[0]] for i in cards2]
    values1, values2 = dict(Counter(values1)), dict(Counter(values2))
    if sorted(list(values1.values())) == [2, 3]:
        if sorted(list(values2.values())) == [2, 3]:
            if max(values1, key=values1.get) > max(values2, key=values2.get):
                return 1
            elif max(values1, key=values1.get) < max(values2, key=values2.get):
                return -1
            elif min(values1, key=values1.get) > min(values2, key=values2.get):
                return 1
            elif min(values1, key=values1.get) < min(values2, key=values2.get):
                return -1
        else:
            return 1
    elif sorted(list(values2.values())) == [2, 3]:
        return -1
    return 0


def flush(cards1, cards2):
    colors1, colors2 = [i[1] for i in cards1], [i[1] for i in cards2]
    values1, values2 = [cards[i[0]] for i in cards1], [cards[i[0]] for i in cards2]
    colors1, colors2 = list(set(colors1)), list(set(colors2))
    if len(colors1) == 1:
        if len(colors2) == 1:
            return high_card(cards1, cards2)
        else:
            return 1
    elif len(colors2) == 1:
        return -1
    return 0


def straight(cards1, cards2):
    values1, values2 = [cards[i[0]] for i in cards1], [cards[i[0]] for i in cards2]
    values1, values2 = sorted(list(set(values1))), sorted(list(set(values2)))
    if len(values1) == 5 and values1[-1] - values1[0] == 4:
        if len(values2) == 5 and values2[-1] - values2[0] == 4:
            return high_card(cards1, cards2)
        else:
            return 1
    elif len(values2) == 5 and values2[-1] - values2[0] == 4:
        return -1
    return 0


def three_of_a_kind(cards1, cards2):
    values1, values2 = [cards[i[0]] for i in cards1], [cards[i[0]] for i in cards2]
    values1, values2 = dict(Counter(values1)), dict(Counter(values2))
    if max(values1.values()) == 3:
        if max(values2.values()) == 3:
            if max(values1, key=values1.get) > max(values2, key=values2.get):
                return 1
            elif max(values1, key=values1.get) < max(values2, key=values2.get):
                return -1
            else:
                return high_card(cards1, cards2)
        else:
            return 1
    elif max(values2.values()) == 3:
        return -1
    return 0


def two_pairs(cards1, cards2):
    values1, values2 = sorted([cards[i[0]] for i in cards1])[::-1], sorted([cards[i[0]] for i in cards2])[::-1]
    if len(list(set(values1))) == 3:
        if len(list(set(values2))) == 3:
            pair_p1, pair_p2 = [], []
            temp_val1, temp_val2 = values1, values2
            while len(temp_val1) > 0:
                if len(temp_val1) > 1:
                    if temp_val1[0] == temp_val1[1]:
                        pair_p1.append(temp_val1[0])
                        temp_val1 = temp_val1[2:]
                    else:
                        temp_val1.pop(0)
                else:
                    temp_val1.pop(0)
            while len(temp_val2) > 0:
                if len(temp_val2) > 1:
                    if temp_val2[0] == temp_val2[1]:
                        pair_p2.append(temp_val2[0])
                        temp_val2 = temp_val2[2:]
                    else:
                        temp_val2.pop(0)
                else:
                    temp_val2.pop(0)
            if max(pair_p1) > max(pair_p2):
                return 1
            elif max(pair_p2) > max(pair_p1):
                return -1
            elif min(pair_p1) > min(pair_p2):
                return 1
            elif min(pair_p2) > min(pair_p1):
                return -1
            else:
                return high_card(cards1, cards2)
        else:
            return 1
    elif len(list(set(values2))) == 3:
        return -1
    return 0


def one_pair(cards1, cards2):
    values1, values2 = sorted([cards[i[0]] for i in cards1])[::-1], sorted([cards[i[0]] for i in cards2])[::-1]
    if len(list(set(values1))) == 4:
        if len(list(set(values2))) == 4:
            p1_max = max(set(values1), key=values1.count)
            p2_max = max(set(values2), key=values2.count)
            if p1_max > p2_max:
                return 1
            elif p2_max > p1_max:
                return -1
            else:
                return high_card(cards1, cards2)
        else:
            return 1
    elif len(list(set(values2))) == 4:
        return -1
    return 0


def high_card(cards1, cards2):
    values1, values2 = sorted([cards[i[0]] for i in cards1])[::-1], sorted([cards[i[0]] for i in cards2])[::-1]
    for a, b in zip(values1, values2):
        if a > b:
            return 1
        elif b > a:
            return -1


value = 0
counter = 0
checks = [royal_flush, straight_flush, four_of_a_kind, full_house, flush, straight, three_of_a_kind, two_pairs,
          one_pair, high_card]

with open("input_data/problem054.txt", "r") as f:
    lines = f.read().splitlines()
    p1_won = 0
    for i in lines:
        value = 0
        counter = 0
        i = i.split(" ")
        player1, player2 = i[:5], i[5:]
        while value == 0 and counter < 10:
            value = checks[counter](player1, player2)
            counter += 1
            if value != 0:
                if value == 1:
                    p1_won += 1
                break
    print(p1_won)
