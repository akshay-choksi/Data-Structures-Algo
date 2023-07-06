
'''
Akshay Choksi (ajc9yr)
9/9/2022
Module 1 Tasks HW
'''

#import what we need
from collections import defaultdict
from collections import deque

'''
4 3
groceryshopping
pickupkids
cookdinner
bedtime
groceryshopping cookdinner
pickupkids cookdinner
cookdinner bedtime
'''

#Read Input
t_length, req_length = input().split()
t_length, req_length = int(t_length), int(req_length)
#Declare our adjacency list
tasks = defaultdict(list)
#Initialize the map for each task's indegree value
count = {}
all_tasks = []

for i in range(t_length):
    all_tasks.append(input())

for j in range(req_length):
    prereq, task = input().split()
    tasks[prereq].append(task)
    count[task] = count.get(task, 0) + 1

queue = deque()
for t in all_tasks:
    if t not in count:
        queue.append(t)

ret = []
while queue:
    node = queue.popleft()
    ret.append(node)
    if node in tasks:
        for vertex in tasks[node]:
            count[vertex] -=1
            if count[vertex] == 0:
                queue.append(vertex)

if len(ret) == t_length:
    retval = (" ".join(ret))
    retval = retval.lstrip()
    retval = retval.rstrip()
    print(retval)
else:
    print(ret)
    print("IMPOSSIBLE")