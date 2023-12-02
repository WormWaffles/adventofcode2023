import os

codes = open('codes.txt', 'r').read().split('\n')

sum = 0
nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

numbers = {"zero": '0',
           "one": '1',
           "two": '2',
           "three": '3',
           "four": '4',
           "five": '5',
           "six": '6',
           "seven": '7',
           "eight": '8',
           "nine": '9'}

for code in codes:
    first = 0
    last = 0
    high = -1
    low = 100000

    for num in nums:
        index_valid_num_low = code.find(num)
        index_valid_num_high = code.rfind(num)
        if index_valid_num_low != -1:
            if index_valid_num_low < low:
                low = index_valid_num_low
                first = num
            if index_valid_num_high > high:
                high = index_valid_num_high
                last = num

    for num in numbers:
        if first is num:
            first = numbers[num]
        if last is num:
            last = numbers[num]

    # print(str(first) + ", " + str(last))            

    # for char in code:
    #     if char in nums and first is None:
    #         first = char
    #     elif char in nums:
    #         last = char
    # if not first:
    #     print("Error: No code: " + code)
    #     exit()
    # if not last:
    #     last = first
    total = first + last
    sum += int(total)

print(sum)