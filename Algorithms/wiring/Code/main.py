'''
Input/Output File
'''

from wiring import *
from node import *

jp, num_connect = input().split()
jp, num_connect = int(jp), int(num_connect)

foundswitch = ""
start_node = Node("")
switch_node = Node("")
node_list = []
switches = []
for junctions in range(jp):
     j1, j2 = input().split()
     j1 = Node(j1)
     j1.ID = j2
     if j2 == "breaker":
        start_node = j1
     if j2 == "switch":
        foundswitch = j1.name
        switch_node = j1
        switches.append(j1)
     if j2 == "light":
        j1.whichSwitch = foundswitch
     node_list.append(j1)
    
w = Connection(jp, start_node)
w.switchlist = switches

# Create blank nodes
node1 = Node("")
node2 = Node("")

for x in range(num_connect):
     c1, c2, weight = input().split()
     c1, c2 = Node(c1), Node(c2)
     weight = int(weight)
     for each_node in node_list:
        if each_node.name == c1.name:
            node1 = each_node
     for itr in node_list:
        if itr.name == c2.name:
            node2 = itr
     if w.isconnected_pre(node1,node2) or w.isconnected_post(node1,node2) or w.isconnected_last(node1,node2):
        w.add_edge(node1, node2, weight)

#print(w.adj)
cost = w.prim()
print(cost)

    
