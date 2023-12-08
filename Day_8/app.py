import re

steps = 0
instructions, map = open('Day_8/directions.txt').read().split('\n\n')
map = re.split('\n| = ', map)
map = {map[i]: map[i + 1] for i in range(0, len(map), 2)}

current_pos = 'AAA'

while current_pos != 'ZZZ':
    for direction in instructions:
        if direction == 'L':
            current_pos = map[current_pos][1:4]
        else:
            current_pos = map[current_pos][6:9]
        steps += 1

print(steps)

# 283 too low