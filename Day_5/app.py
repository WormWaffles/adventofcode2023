almanac = open('Day_5/test_seeds.txt', 'r').read().split('\n')

seeds = almanac[0].split(' ')[1:]
# from empty line to empty line
soil_map = []
line_pos = 3
for line in almanac[line_pos:]:
    if line == '':
        break
    else:
        soil_map.append(line.split(' '))
        line_pos += 1

line_pos += 2
fertilizer_map = []
for line in almanac[line_pos:]:
    if line == '':
        break
    else:
        fertilizer_map.append(line.split(' '))
        line_pos += 1

line_pos += 2
light_map = []
for line in almanac[line_pos:]:
    if line == '':
        break
    else:
        light_map.append(line.split(' '))
        line_pos += 1

line_pos += 2
temp_map = []
for line in almanac[line_pos:]:
    if line == '':
        break
    else:
        temp_map.append(line.split(' '))
        line_pos += 1

line_pos += 2
humidity_map = []
for line in almanac[line_pos:]:
    if line == '':
        break
    else:
        humidity_map.append(line.split(' '))
        line_pos += 1

line_pos += 2
location_map = []
for line in almanac[line_pos:]:
    if line == '':
        break
    else:
        location_map.append(line.split(' '))
        line_pos += 1

print(seeds)
print(soil_map)
print(fertilizer_map)
print(light_map)
print(temp_map)
print(humidity_map)
print(location_map)
print("------------------")

for seed in seeds:
    print(seed)
    for soil in soil_map:
        for rep in range(int(soil[2])):
            if int(seed) == rep + int(soil[0]):
                print(rep + int(soil[0]))
                print("found")
                print(rep)
                print(soil[1])
                print(soil[0])
                seed = rep + int(soil[1])
                break
    print(seed)
    exit()