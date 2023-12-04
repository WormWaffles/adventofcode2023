# Card = winning nums | my nums
cards = open('cards.txt', 'r').read().split('\n')

for card in cards:
    winnings = card.split(':', '|')
    print(winnings)