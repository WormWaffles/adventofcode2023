loop = open('Day_10/test_loop.txt').read().split('\n')

# find 'S' in loop (loop is a list of strings)
y = 0
for i in range(len(loop)):
    x = loop[i].find('S')
    if x != -1:
        y = i
        break

print(loop)