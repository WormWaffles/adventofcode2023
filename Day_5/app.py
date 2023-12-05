almanac = open('Day_5/test_seeds.txt', 'r').read().split('\n')

seeds = almanac[0].split(' ')[1:]

# better way
maps = [seeds.split('')]

print(maps)

# from empty line to empty line
# soil_map = []
# line_pos = 3
# for line in almanac[line_pos:]:
#     if line == '':
#         break
#     else:
#         soil_map.append(line.split(' '))
#         line_pos += 1

# line_pos += 2
# fertilizer_map = []
# for line in almanac[line_pos:]:
#     if line == '':
#         break
#     else:
#         fertilizer_map.append(line.split(' '))
#         line_pos += 1

# line_pos += 2
# water_map = []
# for line in almanac[line_pos:]:
#     if line == '':
#         break
#     else:
#         water_map.append(line.split(' '))
#         line_pos += 1

# line_pos += 2
# light_map = []
# for line in almanac[line_pos:]:
#     if line == '':
#         break
#     else:
#         light_map.append(line.split(' '))
#         line_pos += 1

# line_pos += 2
# temp_map = []
# for line in almanac[line_pos:]:
#     if line == '':
#         break
#     else:
#         temp_map.append(line.split(' '))
#         line_pos += 1

# line_pos += 2
# humidity_map = []
# for line in almanac[line_pos:]:
#     if line == '':
#         break
#     else:
#         humidity_map.append(line.split(' '))
#         line_pos += 1

# line_pos += 2
# location_map = []
# for line in almanac[line_pos:]:
#     if line == '':
#         break
#     else:
#         location_map.append(line.split(' '))
#         line_pos += 1

# print(seeds)
# print(soil_map)
# print(fertilizer_map)
# print(water_map)
# print(light_map)
# print(temp_map)
# print(humidity_map)
# print(location_map)
# print("------------------")

# for i in range(len(seeds)):
#     for soil in soil_map:
#         for rep in range(int(soil[2])):
#             if int(seeds[i]) == rep + int(soil[1]):
#                 seeds[i] = rep + int(soil[0])
#                 break
#     print(seeds[i])
# print("--------")

# for i in range(len(seeds)):
#     for fert in fertilizer_map:
#         for rep in range(int(fert[2])):
#             if int(seeds[i]) == rep + int(fert[1]):
#                 seeds[i] = rep + int(fert[0])
#                 break
#     print(seeds[i])
# print("--------")

# for i in range(len(seeds)):
#     for wtr in water_map:
#         for rep in range(int(wtr[2])):
#             if int(seeds[i]) == rep + int(wtr[1]):
#                 # print(seeds[i])
#                 seeds[i] = rep + int(wtr[0])
#                 break
#         if int(seeds[i]) == rep + int(wtr[1]):
#             print("this")
#             break
#     print(seeds[i])
# print("--------")
