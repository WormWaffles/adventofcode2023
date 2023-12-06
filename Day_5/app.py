import sys

almanac = open('Day_5/seeds.txt', 'r').read().split('\n\n')
seeds = almanac[0].split(' ')[1:]


# progress bar
print("Calculating, this is gonna be a while...\n")
def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[{0}] {1}%  {2}\r'.format(bar, percents, status))
    sys.stdout.flush()


# PART 2 ---------------
maps = []
for i in range(7):
    maps.append(almanac[i+1].split('\n')[1:])

current_seeds = []
lowest = 9223372036854775807
i = 0
while i < len(seeds):
    for idx in range(int(seeds[i+1])):
        current_seeds.append(int(seeds[i]) + idx)
    # calc here
    for i in range(len(maps)):
        progress(0, 100, status='')
        for j in range(len(current_seeds)):
            progress(j, len(current_seeds), status='')
            # calculate each map here
            for map in maps[i]:
                if int(current_seeds[j]) >= int(map.split(' ')[1]) and int(current_seeds[j]) <= int(map.split(' ')[1]) + int(map.split(' ')[2]) - 1:
                    current_seeds[j] = str(int(map.split(' ')[0]) + int(current_seeds[j]) - int(map.split(' ')[1]))
                    break
    for pos in current_seeds:
        if int(pos) < lowest:
            lowest = int(pos)
    current_seeds = []
    i += 2
progress(100, 100, status='')
print("\n\nLowest location is: " + str(lowest))