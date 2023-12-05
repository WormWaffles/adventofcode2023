import sys

# Card = winning nums | my nums
cards = open('Day_4/cards.txt', 'r').read().split('\n')

sum = 0
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

print("Sum of points: " + str(sum))
print("\ncalculating # of cards...")

def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[{0}] {1}%  {2}\r'.format(bar, percents, status))
    sys.stdout.flush()

progress(0, 190, status='')

def count(card, idx):
    buffer = 0
    for num in card[1]:
        valid = False
        if num in card[0]:
            valid = True
            break
    if not valid:
        return 0
    for num in card[1]:
        if num in card[0]:
            buffer += 1
    total = 0
    for i in range(buffer):
        idx += 1
        total += 1 + count(formated_cards[idx], idx)
    return total

idx = 0
for card in formated_cards:
    total_cards += 1 + count(formated_cards[card], idx)
    progress(idx, 190, status='')
    idx += 1

progress(190, 190, status='')
print("\n\nTotal cards: " + str(total_cards))