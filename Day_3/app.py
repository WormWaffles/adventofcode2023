scheme = open('Day_3/scheme.txt', 'r').read().split('\n')

grid = []*len(scheme)
line_len = None
grid_width = 0

sum = 0

nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
nono_square = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']

for line in scheme:
    line = list(line)
    line_len = len(line)
    grid.append(line)
    grid_width += 1

idx = 0
idy = 0
for idx in range(line_len):
    for idy in range(grid_width):
        # if char is not a num or .
        if grid[idx][idy] not in nono_square:
            # check each position around the char
            if grid[idx-1][idy-1] in nums:
                current_num = grid[idx-1][idy-1]
                if grid[idx-1][idy-2] in nums:
                    current_num = grid[idx-1][idy-2] + current_num
                if grid[idx-1][idy-3] in nums:
                    current_num = grid[idx-1][idy-3] + current_num
                if grid[idx-1][idy] in nums:
                    current_num = current_num + grid[idx-1][idy]
                if grid[idx-1][idy+1] in nums:
                    current_num = current_num + grid[idx-1][idy+1]
                print(current_num)
                sum += int(current_num)
            # if grid[idx][idy-1] in nums:
            #     current_num = grid[idx][idy-1]
            #     if grid[idx][idy-2] in nums:
            #         current_num = grid[idx][idy-2] + current_num
            #     if grid[idx][idy-3] in nums:
            #         current_num = grid[idx][idy-3] + current_num
            #     if grid[idx][idy] in nums:
            #         current_num = current_num + grid[idx][idy]
            #     if grid[idx][idy+1] in nums:
            #         current_num = current_num + grid[idx][idy+1]
            #     print(current_num)
            #     sum += int(current_num)
            if grid[idx+1][idy-1] in nums:
                current_num = grid[idx+1][idy-1]
                if grid[idx+1][idy-2] in nums:
                    current_num = grid[idx+1][idy-2] + current_num
                if grid[idx+1][idy-3] in nums:
                    current_num = grid[idx+1][idy-3] + current_num
                if grid[idx+1][idy] in nums:
                    current_num = current_num + grid[idx+1][idy]
                if grid[idx+1][idy+1] in nums:
                    current_num = current_num + grid[idx+1][idy+1]
                print(current_num)
                sum += int(current_num)
            if grid[idx-1][idy] in nums:
                current_num = grid[idx-1][idy]
                if grid[idx-1][idy-1] in nums:
                    current_num = grid[idx-1][idy-1] + current_num
                if grid[idx-1][idy-2] in nums:
                    current_num = grid[idx-1][idy-2] + current_num
                if grid[idx-1][idy+1] in nums:
                    current_num = current_num + grid[idx-1][idy+1]
                if grid[idx-1][idy+2] in nums:
                    current_num = current_num + grid[idx-1][idy+2]
                print(current_num)
                sum += int(current_num)
            if grid[idx+1][idy] in nums:
                current_num = grid[idx+1][idy]
                if grid[idx+1][idy-1] in nums:
                    current_num = grid[idx+1][idy-1] + current_num
                if grid[idx+1][idy-2] in nums:
                    current_num = grid[idx+1][idy-2] + current_num
                if grid[idx+1][idy+1] in nums:
                    current_num = current_num + grid[idx+1][idy+1]
                if grid[idx+1][idy+2] in nums:
                    current_num = current_num + grid[idx+1][idy+2]
                print(current_num)
                sum += int(current_num)
            if grid[idx-1][idy+1] in nums:
                current_num = grid[idx-1][idy+1]
                if grid[idx-1][idy] in nums:
                    current_num = grid[idx-1][idy] + current_num
                if grid[idx-1][idy-1] in nums:
                    current_num = grid[idx-1][idy-1] + current_num
                if grid[idx-1][idy+2] in nums:
                    current_num = current_num + grid[idx-1][idy+2]
                if grid[idx-1][idy+3] in nums:
                    current_num = current_num + grid[idx-1][idy+3]
                sum += int(current_num)
                print(current_num)
            if grid[idx][idy+1] in nums:
                current_num = grid[idx][idy+1]
                if grid[idx][idy] in nums:
                    current_num = grid[idx][idy] + current_num
                if grid[idx][idy-1] in nums:
                    current_num = grid[idx][idy-1] + current_num
                if grid[idx][idy+2] in nums:
                    current_num = current_num + grid[idx][idy+2]
                if grid[idx][idy+3] in nums:
                    current_num = current_num + grid[idx][idy+3]
                print(current_num)
                sum += int(current_num)
            if grid[idx+1][idy+1] in nums:
                current_num = grid[idx+1][idy+1]
                if grid[idx+1][idy] in nums:
                    current_num = grid[idx+1][idy] + current_num
                if grid[idx+1][idy-1] in nums:
                    current_num = grid[idx+1][idy-1] + current_num
                if grid[idx+1][idy+2] in nums:
                    current_num = current_num + grid[idx+1][idy+2]
                if grid[idx+1][idy+3] in nums:
                    current_num = current_num + grid[idx+1][idy+3]
                print(current_num)
                sum += int(current_num)
print(sum)
