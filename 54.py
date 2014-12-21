import time
import helpers
import math

inputFile = open('resources/p054_poker.txt', 'r')

start = time.clock()

figures = {'A': 14, 'T': 10, 'J': 11, 'Q': 12, 'K': 13}


def getPair(pair):
    value = pair[0]
    if not value.isdigit() or value == 10:
        value = figures[value]
    return {'suit': pair[1], 'value': int(value)}


def getHands(line):
    hands = {'playerA': [], 'playerB': []}
    i = 0
    for pair in line.split(' '):
        hands['playerA' if i < 5 else 'playerB'].append(getPair(pair))
        i += 1
    return hands

def getPairs(hand):
    vals = values(hand)
    vals.sort()
    p = [{'v': None, 'p': 0}, {'v': None, 'p': 0}]

    fop = False
    pairNum = 0
    for k, v in enumerate(vals[1:]):
        if v == vals[k]:
            fop = True
            if p[pairNum]['p'] == 0: p[pairNum]['p'] = 1
            p[pairNum]['p'] += 1
            p[pairNum]['v'] = v
        elif (fop is True):
            pairNum = 1
    p.sort(key=lambda p: p['p'])

    return p


def sumFigures(hand):
    sum = 0
    for pair in hand:
        sum += pair['value']
    return sum


def values(hand):
    return [a['value'] for a in hand]


def checkStraight(vals):
    vals.sort()
    for k, v in enumerate(vals[1:]):
        if v - vals[k] != 1:
            return False
    return True


def isStraight(hand):
    vals = values(hand)
    _isStraight = checkStraight(vals)
    if _isStraight:
        return [True, max(vals)]
    else:
        if vals.count(14) > 0:
            Aindex = vals.index(14) >= 0
            vals[Aindex] = 1
            vals.sort()
            _isStraight = checkStraight(vals)
            if _isStraight:
                return [True, max(vals)]
    return [False, 0]


def isSameSuit(hand):
    suits = [a['suit'] for a in hand]
    for k, v in enumerate(suits[1:]):
        if v != suits[k]:
            return False
    return True


def getMaxValue(hand):
    return max(values(hand))


def calcHand(hand):
    figureSum = sumFigures(hand)
    pairs = getPairs(hand)
    maxValue = getMaxValue(hand)
    _isStraight = isStraight(hand)
    _isSameSuit = isSameSuit(hand)

    _isRoyalFlush = _isSameSuit and _isStraight and figureSum == 60
    _isStraightFlush = _isSameSuit and _isStraight[0]
    _isFourOfAKind = pairs[1] == 4
    _isFullHouse = pairs[1]['p'] == 3 and pairs[0]['p'] == 2
    _isFlush = _isSameSuit
    _isStraight = _isStraight
    _isThreeOfAKind = pairs[1]['p'] == 3 and pairs[0]['p'] == 0
    _isTwoPairs = pairs[0]['p'] == 2 and pairs[1]['p'] == 2
    _isOnePair = pairs[1]['p'] == 2 and pairs[0]['p'] == 0
    _values = sorted(values(hand),None,None,True)

    result = _values
    result = [pairs[1]['v'] if _isOnePair else pairs[0]['v'] if  _isTwoPairs else 0] + result
    result = [pairs[1]['v'] if _isTwoPairs else 0] + result
    result = [pairs[1]['v'] if _isThreeOfAKind else 0] + result
    result = [_isStraight[1] if _isStraight[0] else 0] + result
    result = [1 if _isFlush else 0] + result
    result = [pairs[0]['v'] if _isFullHouse else 0] + result
    result = [pairs[1]['v'] if _isFullHouse else 0] + result
    result = [pairs[1]['v'] if _isFourOfAKind else 0] + result
    result = [maxValue if _isRoyalFlush else 0] + result

    strResult = []
    for i, v in enumerate(result):
        strResult.append(str(v).zfill(2))
    return int(''.join(strResult))


handAWins = 0

for line in inputFile.readlines():
    line = line.strip('\n')
    hands = getHands(line)
    handA = calcHand(hands['playerA'])
    handB = calcHand(hands['playerB'])
    if handA > handB:
        handAWins += 1
print handAWins
print time.clock() - start