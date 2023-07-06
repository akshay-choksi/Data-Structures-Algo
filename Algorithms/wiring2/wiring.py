'''
Akshay Choksi (ajc9yr)
Solution for Module 2 HW: Wiring with Prim's Algorithn
'''

import heapq
import random

#Global Variables
start = ""
known = set()
junctions = []

#only add valid nodes to the PQ
#List of junctions
#While PQ and len(visited) < len(junctions):
    #for i in range(len(neigbors)):
    #   junction2 = neighbors[i]
    #   if self.isConnectable(curr, neighbor) and !neighbor.known():
            #PQ.heappush((costs[i], neighbor))

class Junction:
    def __init__(self):
        self.name = ""
        self.type = ""
        self.neighbors = []
        self.costs = []
        self.known = False
        self.whichSwitch = ""

class Wiring:
    def preSwitch(self,j1):
        return j1.type == "breaker" or j1.type == "outlet" or j1.type == "box"

    def isSwitch(self,j1):
        return j1.type == "switch"

    def postSwitch(self,j1):
        return j1.type == "light"

    def connectable(self,j1,j2):
        if self.preSwitch(j1) and self.preSwitch(j2):
            return True

    def connectable2(self, j1, j2):
        if self.preSwitch(j1) and self.isSwitch(j2):
            return True
        
    def connectable3(self, j1, j2):
        if self.isSwitch(j1) and self.postSwitch(j2):
            if j2.whichSwitch == j1.name:
                return True
        if self.postSwitch(j1) and self.postSwitch(j2):
            if j1.whichSwitch == j2.whichSwitch:
                return True
        return False

junction_num, edge_num = input().split()
junction_num, edge_num = int(junction_num), int(edge_num)

graph = {}
switchName = ""
for i in range(junction_num):
    name, type = input().split()
    node = Junction()
    node.type = type
    node.name = name
    if type == "switch":
        switchName = name
    if type == "breaker":
        start = name
    node.whichSwitch = switchName
    graph[node.name] = node

for j in range(edge_num):
    node1, node2, cost = input().split()
    cost = int(cost)
    junction1 = graph[node1]
    junction2 = graph[node2]
    junction1.costs.append(cost)
    junction2.costs.append(cost)
    junction1.neighbors.append(junction2) 
    junction2.neighbors.append(junction1)
    graph[node1] = junction1
    graph[node2] = junction2

# print(graph["j1"].neighbors[0].name)
# print(graph["j1"].costs[0])

w = Wiring()

start_breaker = graph[start]
for key in graph.values():
    junctions.append(key)

heap = [(0, random.randint(1, 10000000), start_breaker)]
heapq.heapify(heap)
cost = 0
heap2 = []
while(heap and len(known) < len(junctions)):
    dist, discard, j1 = heapq.heappop(heap)
    if j1 not in known:
        known.add(j1)
        cost+=dist
        for i in range(len(j1.neighbors)):
            j2 = j1.neighbors[i]
            new_cost = j1.costs[i]
            if w.connectable(j1, j2) and j2 not in known:
                heapq.heappush(heap, (new_cost,random.randint(1,1000000), j2))
            if w.connectable2(j1,j2) and j2 not in known:
                heapq.heappush(heap2, (new_cost,random.randint(1,1000000), j2))


heap3 = []
while(heap2 and len(known) < len(junctions)):
    dist, discard, j1 = heapq.heappop(heap2)
    if j1 not in known:
        known.add(j1)
        cost+=dist
        for i in range(len(j1.neighbors)):
            j2 = j1.neighbors[i]
            new_cost = j1.costs[i]
            if w.connectable3(j1,j2) and j2 not in known:
                heapq.heappush(heap3, (new_cost,random.randint(1,1000000), j2))

while(heap3 and len(known) < len(junctions)):
    dist, discard, j1 = heapq.heappop(heap3)
    if j1 not in known:
        known.add(j1)
        cost+=dist
        for i in range(len(j1.neighbors)):
            j2 = j1.neighbors[i]
            new_cost = j1.costs[i]
            if w.connectable3(j1,j2) and j2 not in known:
                heapq.heappush(heap3, (new_cost,random.randint(1,1000000), j2))

print(cost)








   
   
    
