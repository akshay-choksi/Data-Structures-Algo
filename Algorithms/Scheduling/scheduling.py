'''
Akshay Choksi (ajc9yr)
12/5/2022
Solution with Ford-Fulkerson for Bi-Partite Matching
'''
'''
r = # of requests
c = # of courses
n = required enrollment (value for source to student)
'''
from collections import defaultdict, deque
import math
'''
9 3 2
Alice CS_2102
Alice CS_3102
Alice CS_4102
Bob CS_2102
Bob CS_3102
Charlie CS_2102
Charlie CS_4102
David CS_2102
David CS_3102
CS_2102 3
CS_3102 3
CS_4102 3

4 2 1
Alice CS_2102
Alice CS_3102
Charlie CS_2102
Bob CS_2102
CS_2102 1
CS_3102 1

0 0 0
'''


def BFS(graph, path, source, sink):

    # Create a queue and visited set
    queue = deque()
    visited = set()
    queue.append(source)
    visited.add(source)

    while queue:
        node = queue.popleft()
        for i in range(len(graph[node])):
            flow = graph[node][i]
            if flow > 0 and i not in visited:
                visited.add(i)
                queue.append(i)
                #add to path
                path[i] = node
                if i == sink:
                    return True
    return False
            
def ford_fulkerson(graph,  source, sink):
    
    max_flow = 0    
    path = [-10000]*(len(graph))

    while BFS(graph, path, source, sink) == True:
        cur_flow = math.inf
        s = sink
        while(s !=  source):
            cur_flow = min(graph[path[s]][s],cur_flow)
            s = path[s]
        max_flow+=cur_flow
        y = sink
        while(y !=  source):
            x = path[y]
            graph[x][y] -= cur_flow
            graph[y][x] += cur_flow
            y = path[y]
        cur_flow = math.inf
    return max_flow
while(True):
    requests, courses, n = input().split()
    requests, courses, n = int(requests), int(courses), int(n)
    if requests == 0 and courses == 0 and n == 0:
        break
    values = []
    students = defaultdict(list)
    capacities = {} #set value as edge from course to sink

    for i in range(requests):
        name, course = input().split()
        students[name].append(course)

    for j in range(courses):
        name, capacity = input().split()
        capacity = int(capacity)
        capacities[name] = capacity
    null = input()
    student_number = len(students)
    node_count = student_number + courses + 2
    graph = [[0 for x in range(node_count)] for y in range(node_count)]

    #set first row student values to n
    for i in range(1, student_number + 1):
        graph[0][i] = n

    people = list(students.keys())

    counter = 1
    keys = list(students.keys())

    for key in keys:
        students[counter] = students[key]
        del students[key]
        counter+=1

    keys = list(capacities.keys())
    class_to_index = {}

    for key in keys:
        class_to_index[key] = counter
        capacities[counter] = capacities[key]
        del capacities[key]
        counter+=1

    for i in range(1, student_number + 1):
        for val in students[i]:
            graph[i][class_to_index[val]] = 1

    for i in range(student_number+1, len(graph) - 1):
        graph[i][len(graph) - 1] = capacities[i]


    ret = ford_fulkerson(graph, 0, len(graph) - 1)
    if ret == n * student_number:
        print("Yes")
    else:
        print("No")
