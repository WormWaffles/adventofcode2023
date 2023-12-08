from collections import Counter
import operator

hands = [x.split(' ') for x in open('Day_7/test_hands.txt').read().split('\n')]
cards = {'A':13, 'K':12, 'Q':11, 'T':10, '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2, 'J':1}

# number to represend hand value 
for hand in hands:
    card_values = hand[0]
    value = 0 # will be the card value

    # check for hand value
    char_count = Counter(card_values)
    nums = dict(char_count)
    first = max(nums.items(), key=operator.itemgetter(1))[1]
    
    if first == 5: # 5 of a kind
        value += 60000000000
    else:
        nums.pop(max(nums.items(), key=operator.itemgetter(1))[0])
        second = max(nums.items(), key=operator.itemgetter(1))[1]
        if first == 4:
            value += 50000000000
        elif first == 3 and second == 2:
            value += 40000000000
        elif first == 3:
            value += 30000000000
        elif first == 2 and second == 2:
            value += 20000000000
        elif first == 2:
            value += 10000000000

    # part 2 'J'
    count_j = 0
    for x in hand[0]:
        if x == 'J':
            count_j += 1
    if count_j == 4:
        value += 10000000000
    elif count_j == 3 and second == 2:
        value += 30000000000
    elif count_j == 3 and second == 1:
        value += 20000000000
    elif count_j == 2 and second == 2:
        value += 30000000000
    elif count_j == 2:
        value += 20000000000
    elif count_j == 1 and first == 4:
        value += 10000000000
    elif count_j == 1 and first == 3:
        value += 10000000000
    elif count_j == 1 and first == 2 and second == 2:
        value += 20000000000
    else:
        value += 20000000000
    pos = [8, 6, 4, 2, 0]
    value += sum([int(str(cards.get(card_values[x])) + ('0' * pos[x])) for x in range(len(card_values))])
    hand.append(value)

# print(hands)

def Sort(sub_li):
    sub_li.sort(key = lambda x: x[2])
    return sub_li
hands = Sort(hands)

total_winnings = 0
for idx in range(len(hands)):
    total_winnings += int(hands[idx][1]) * (idx + 1)

print(total_winnings)

# 251228163 too high
# 251231239 too high
# 252267124