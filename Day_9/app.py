codes = open('Day_9/codes.txt').read().split('\n')
codes = [code.split(' ') for code in codes]

def find_next(arr):
    # if all arr is 0
    if arr.count(0) == len(arr):
        return 0
    arr2 = [int(arr[i+1]) - int(arr[i]) for i in range(len(arr)-1)]
    return int(arr[len(arr)-1]) + find_next(arr2)

sum = 0
for code in codes:
    sum += find_next(code)

print(sum)