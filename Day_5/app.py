almanac = open('Day_5/test_seeds.txt', 'r').read().split('\n\n')

seeds = almanac[0].split(' ')[1:]

# better way
maps = []
for i in range(7):
    maps.append(almanac[i+1].split('\n')[1:])

lowest = 9223372036854775807
for i in range(len(maps)):
    for j in range(len(seeds)):
        # calculate each map here
        for map in maps[i]:
            if int(seeds[j]) >= int(map.split(' ')[1]) and int(seeds[j]) <= int(map.split(' ')[1]) + int(map.split(' ')[2]) - 1:
                seeds[j] = str(int(map.split(' ')[0]) + int(seeds[j]) - int(map.split(' ')[1]))
                if int(seeds[j]) < lowest:
                    lowest = int(seeds[j])
                break
print("Lowest location is: " + str(lowest))