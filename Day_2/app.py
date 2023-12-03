# 12 red 13 green 14 blue
games = open("games.txt", 'r').read().split('\n')

max_vals = [12, 13, 14]

sum = 0
total_power = 0

for game in games:
    # split game by colon
    hands = game.split('; ')
    front = hands[0].split(': ')

    # cut game name off front and get game num
    hands[0] = front[1]
    game_num = front[0].split(' ')[1]

    is_valid = True

    # loop through each hand
    for hand in hands:
        cubes = hand.split(', ')
        # loop through each cube in hand
        for cube in cubes:
            cube = cube.split(' ')
            if cube[1] == "red":
                if int(cube[0]) > 12:
                    is_valid = False
            elif cube[1] == "green":
                if int(cube[0]) > 13:
                    is_valid = False
            elif cube[1] == "blue":
                if int(cube[0]) > 14:
                    is_valid = False
            else:
                print("Error: Color not valid.")

    if is_valid:
        sum += int(game_num)

    # part two
    game_power = 0
    red = 0
    green = 0
    blue = 0

    for hand in hands:
        cubes = hand.split(', ')
        for cube in cubes:
            cube = cube.split(' ')
            if cube[1] == "red":
                if int(cube[0]) > red:
                    red = int(cube[0])
            elif cube[1] == "green":
                if int(cube[0]) > green:
                    green = int(cube[0])
            elif cube[1] == "blue":
                if int(cube[0]) > blue:
                    blue = int(cube[0])
            else:
                print("Error: Color not valid.")

    game_power = red * green * blue
    total_power += game_power
        

print("Sum of valid games: " + str(sum))
print("Total power: " + str(total_power))