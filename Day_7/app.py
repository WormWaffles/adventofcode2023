from collections import Counter
import operator

hands = [x.split(' ') for x in open('Day_7/test_hands.txt').read().split('\n')]
cards = {'A':14, 'K':13, 'Q':12, 'J':11, 'T':10, '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2}

# number to represend hand value 
for hand in hands:
    card_values = hand[0]
    value = 0 # will be the card value

    # check for hand value
    char_count = Counter(card_values)
    # print(char_count)
    nums = dict(char_count)
    first = max(nums.items(), key=operator.itemgetter(1))[1]
    # nums.pop(max(nums.items(), key=operator.itemgetter(1))[0])
    # second = max(nums.items(), key=operator.itemgetter(1))[1]


    # print(first)
    # print(second)
    if first > 4:
        value += 6000000
    else:
        nums.pop(max(nums.items(), key=operator.itemgetter(1))[0])
        second = max(nums.items(), key=operator.itemgetter(1))[1]
    if first == 3:
        value += 5000000
    elif first == 3 and second == 2:
        value += 4000000
    elif first == 2 and second == 3:
        value += 4000000
    elif first == 3:
        value += 3000000
    elif first == 2 and second == 2:
        value += 2000000
    elif first == 2:
        value += 1000000
    # print(first)
    # print(second)

    pos = [4, 3, 2, 1, 0]
    value += sum([int(str(cards.get(card_values[x])) + ('0' * pos[x])) for x in range(len(card_values))])
    print(value)
    hand.append(value)

print(hands)

def Sort(sub_li):
    sub_li.sort(key = lambda x: x[2])
    return sub_li

print(Sort(hands))

# 32T3K 765 -> two of a kind so starts with 2 then first card value 3 then 2 then 10 then 3 then 13
# 100000
#  30000
#   2000
#   1000
#     30
#     14
# 133043 value 1
# T55J5 684 4
# KK677 28 3
# KTJJT 220 2
# QQQJA 483 5