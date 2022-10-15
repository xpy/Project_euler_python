import time
import helpers
import math

inputFile = open('resources/p054_poker.txt', 'r')

start = time.perf_counter()

figures = {'A': 14, 'T': 10, 'J': 11, 'Q': 12, 'K': 13}


def get_pair(pair):
    value = pair[0]
    if not value.isdigit() or value == 10:
        value = figures[value]
    return {'suit': pair[1], 'value': int(value)}


def get_hands(line):
    hands = {'playerA': [], 'playerB': []}
    i = 0
    for pair in line.split(' '):
        hands['playerA' if i < 5 else 'playerB'].append(get_pair(pair))
        i += 1
    return hands


def get_pairs(hand):
    vals = values(hand)
    vals.sort()
    p = [{'v': None, 'p': 0}, {'v': None, 'p': 0}]

    fop = False
    pair_num = 0
    for k, v in enumerate(vals[1:]):
        if v == vals[k]:
            fop = True
            if p[pair_num]['p'] == 0:
                p[pair_num]['p'] = 1
            p[pair_num]['p'] += 1
            p[pair_num]['v'] = v
        elif fop is True:
            pair_num = 1
    p.sort(key=lambda p: p['p'])

    return p


def sum_figures(hand):
    num_sum = 0
    for pair in hand:
        num_sum += pair['value']
    return num_sum


def values(hand):
    return [a['value'] for a in hand]


def check_straight(vals):
    vals.sort()
    for k, v in enumerate(vals[1:]):
        if v - vals[k] != 1:
            return False
    return True


def is_straight(hand):
    vals = values(hand)
    _isStraight = check_straight(vals)
    if _isStraight:
        return [True, max(vals)]
    else:
        if vals.count(14) > 0:
            a_index = vals.index(14) >= 0
            vals[a_index] = 1
            vals.sort()
            _isStraight = check_straight(vals)
            if _isStraight:
                return [True, max(vals)]
    return [False, 0]


def is_same_suit(hand):
    suits = [a['suit'] for a in hand]
    for k, v in enumerate(suits[1:]):
        if v != suits[k]:
            return False
    return True


def get_max_value(hand):
    return max(values(hand))


def calc_hand(hand):
    figure_sum = sum_figures(hand)
    pairs = get_pairs(hand)
    max_value = get_max_value(hand)
    _isStraight = is_straight(hand)
    _isSameSuit = is_same_suit(hand)

    _isRoyalFlush = _isSameSuit and _isStraight and figure_sum == 60
    _isStraightFlush = _isSameSuit and _isStraight[0]
    _isFourOfAKind = pairs[1] == 4
    _isFullHouse = pairs[1]['p'] == 3 and pairs[0]['p'] == 2
    _isFlush = _isSameSuit
    _isStraight = _isStraight
    _isThreeOfAKind = pairs[1]['p'] == 3 and pairs[0]['p'] == 0
    _isTwoPairs = pairs[0]['p'] == 2 and pairs[1]['p'] == 2
    _isOnePair = pairs[1]['p'] == 2 and pairs[0]['p'] == 0
    _values = sorted(values(hand), None, None, True)

    result = _values
    result = [pairs[1]['v'] if _isOnePair else pairs[0]['v'] if _isTwoPairs else 0] + result
    result = [pairs[1]['v'] if _isTwoPairs else 0] + result
    result = [pairs[1]['v'] if _isThreeOfAKind else 0] + result
    result = [_isStraight[1] if _isStraight[0] else 0] + result
    result = [1 if _isFlush else 0] + result
    result = [pairs[0]['v'] if _isFullHouse else 0] + result
    result = [pairs[1]['v'] if _isFullHouse else 0] + result
    result = [pairs[1]['v'] if _isFourOfAKind else 0] + result
    result = [max_value if _isRoyalFlush else 0] + result

    str_result = []
    for i, v in enumerate(result):
        str_result.append(str(v).zfill(2))
    return int(''.join(str_result))


handAWins = 0

for line in inputFile.readlines():
    line = line.strip('\n')
    hands = get_hands(line)
    handA = calc_hand(hands['playerA'])
    handB = calc_hand(hands['playerB'])
    if handA > handB:
        handAWins += 1
print(handAWins)
print(time.perf_counter() - start)
