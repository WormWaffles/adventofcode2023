# time and distance array
time, distance = open('Day_6/times.txt').read().split('\n')
# time = time.split(' ')[1:]
# while '' in time:
#     time.remove('')
# distance = distance.split(' ')[1:]
# while '' in distance:
#     distance.remove('')

# part 2
time = int(time[5:].replace(' ', ''))
distance = int(distance[10:].replace(' ', ''))
count = 0


high = time
low = 0
mili = (low + high) // 2
while low <= high:
    if (time - mili) * mili > distance:
        high = mili - 1
    else:
        low = mili + 1
    mili = (low + high) // 2
bottom = low

high = time
low = 0
mili = (low + high) // 2
while low <= high:
    if (time - mili) * mili > distance:
        low = mili + 1
    else:
        high = mili - 1
    mili = (low + high) // 2
top = high

print("You can beat the race " + str(top - bottom + 1) + " times.")