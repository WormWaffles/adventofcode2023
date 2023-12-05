# Card = winning nums | my nums
cards = open('Day_4/cards.txt', 'r').read().split('\n')

sum = 0
# total_cards = len(cards)
total_cards = 0

for card in cards:
    numbers = card.replace('|', ':').split(':')
    winnings = numbers[1]
    my_nums = numbers[2]
    winnings = winnings.replace('  ', ' ').split(' ')
    while '' in winnings:
        winnings.remove("")
    winnings = [int(i) for i in winnings]
    my_nums = my_nums.replace('  ', ' ').split(' ')
    while '' in my_nums:
        my_nums.remove('')
    my_nums = [int(i) for i in my_nums]

    # check for winning numbers
    score = 0
    for num in my_nums:
        if num in winnings:
            if score == 0:
                score = 1
            else:
                score *= 2
            
    sum += score

# part 2 (if a card wins, it wins that number of cards in front of it...)
formated_cards = {}
for i in range(len(cards)):

    numbers = cards[i].replace('|', ':').split(':')
    front = numbers[1]
    back = numbers[2]

    # front = numbers[1] + '|' + numbers[2]
    front = front.replace('  ', ' ').split(' ')
    back = back.replace('  ', ' ').split(' ')

    while '' in front:
        front.remove('')
    while '' in back:
        back.remove('')

    formated_cards[i] = [front, back]

def count(card, idx):
    for num in card[0]:
        valid = True
        if num not in card[1]:
            valid = False
    if not valid:
        return 0
    for num in card[1]:
        if num in card[0]:
            idx += 1
            print(idx)
            return 1 + count(formated_cards[idx], idx)

for card in formated_cards:
    idx = 0
    total_cards += count(formated_cards[card], idx)
    # print(total_cards)
    exit()

# print(sum)
print(total_cards)
# 595 too low