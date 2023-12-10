import re
import math

instructions, map = open('Day_8/directions.txt').read().split('\n\n')
map = re.split('\n| = ', map)
map = {map[i]: map[i + 1] for i in range(0, len(map), 2)}

current_pos = []
for x in map:
    if x[2] == 'A':
        current_pos.append(x)

print("Loading...")
# part 2
start_count = False
loop_time = [0 for i in current_pos]
for idx in range(len(current_pos)):
    steps = 0
    while loop_time[idx] == 0:
        for direction in instructions:
            if direction == 'L':
                current_pos[idx] = map[current_pos[idx]][1:4]
            else:
                current_pos[idx] = map[current_pos[idx]][6:9]
            if not start_count and current_pos[idx][2] == 'Z':
                start_count = True
            if start_count:
                if current_pos[idx][2] == 'Z' and steps > 0:
                    loop_time[idx] = steps
                    start_count = False
                steps += 1
print(loop_time)

steps = 1
lcm = math.lcm(*[x for x in loop_time])

print(lcm)

# 26559759536163661731943307 too high
# 39511276923116954201400 too high
# 4140929357167498 Nope
# 14631604759649
# 20659 too low