codes = open('Day_9/codes.txt').read().split('\n')
codes = [code.split(' ') for code in codes]

def find_next(arr):
    # if all arr is 0
    if arr.count(0) == len(arr):
        return 0
    arr2 = [int(arr[i+1]) - int(arr[i]) for i in range(len(arr)-1)]
    return int(arr[len(arr)-1]) + find_next(arr2)

def find_prev(arr):
    # if all arr is 0
    if arr.count(0) == len(arr):
        return 0
    arr2 = [int(arr[i+1]) - int(arr[i]) for i in range(len(arr)-1)]
    return int(arr[0]) - find_prev(arr2)

sum_next = 0
sum_prev = 0
for code in codes:
    sum_next += find_next(code)
    sum_prev += find_prev(code)


print(sum_next)
print(sum_prev)