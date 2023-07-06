'''
Akshay Choksi (ajc9yr)
Solving Daycare (Greedy Algorithm)
'''

'''
Increasing: Smallest original Room Size 

Same: Does not matter

Decreasing: Biggest new room size
'''
ret = []
for i in range(2):
    increasing = []
    same = []
    decreasing = []
    room_number = int(input())
    for j in range(room_number):
        old, new = input().split()
        old, new = int(old), int(new)
        if old < new:
            increasing.append([old,new])
        elif old == new:
            same.append([old, new])
        else:
            decreasing.append([old,new])

    trailer_capacity = 0
    extra_space = 0

    #sort for greedy
    if increasing:
        increasing.sort(key=lambda x: x[0])
    if decreasing:
        decreasing.sort(key=lambda y: y[1])
        decreasing.reverse()

    rooms = increasing + same + decreasing

    for c1, c2 in rooms:
        diff = c1 - extra_space
        if diff <= 0:
            extra_space -= c1
        else:
            extra_space = 0
            trailer_capacity += diff
        extra_space+=c2

    ret.append(trailer_capacity)

for val in ret:
    print(val)
