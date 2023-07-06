 from collections import defaultdict
from node import *
import math

class Wiring:
    def __init__(self) -> None:
        self.costs = []
        self.nodes = []
        self.visited = []
        self.nodeIndex = {}
        self.light_switch = {}
        self.start = ""

    def input(self):
        j_count, num_connect = input().split()
        j_count, num_connect = int(j_count), int(num_connect)

        for i in range(j_count):
            name, type = input().split()
            if(type == 'breaker'):
                self.start = name
            junction = Node(name,type)
            if type == "switch":
                switch_cur = junction
            if(type == "light"):
                self.light_switch[junction.name] = switch_cur.name
            self.nodes.append(junction)
            self.nodeIndex[name] = i
            self.visited.append(False)
            self.costs.append(math.inf)
        for j in range(num_connect):
            node1, node2, cost = input().split()
            cost = int(cost)

            index1 = self.nodeIndex[node1]
            index2 = self.nodeIndex[node2]
            if (index1 > len(self.nodeIndex) or index2 > len(self.nodeIndex)):
                continue
            n1 = self.nodes[index1]
            n2 = self.nodes[index2]

            if self.preSwitch(n1) and self.postSwitch(n2):
                continue
            if self.postSwitch(n1) and self.preSwitch(n2):
                continue
            if self.postSwitch(n1) and self.isSwitch(n2):
                continue
            if self.isSwitch(n1) and self.preSwitch(n2):
                continue
            if self.preSwitch(n1) and self.isSwitch(n2):
                n1.adj.append(n2)
                n1.weights.append(cost)
                continue
            if self.postSwitch(n1) and self.postSwitch(n2):
                if self.light_switch[n1] == self.light_switch[n2]:
                    n1.adj.append(n2)
                    n1.weights.append(cost)
                else:
                    continue
            if(self.isSwitch(n1) and self.postSwitch(n2)):
                if n1.name == self.light_switch[n2.name]:
                    n1.adj.append(n2)
                    n1.weights.append(cost)
                else:
                    continue

        n1.adj.append(n2)
        n1.weights.append(cost)

        n2.adj.append(n1)
        n2.weights.append(cost)

    def findMin(self):
        ret = -1
        min = math.inf
        pre = False
        for i in range(len(self.costs)):
            node1 = self.nodes[i]
            if self.preSwitch(node1) and self.costs[i] < min and self.visited[i] == False:
                min = self.costs[i]
                ret = i
                pre = True
        if pre:
            return ret
        for j in range(len(self.costs)):
            if self.costs[i] < min and self.visited == False:
                min = self.costs[j]
                ret = j
        return ret
            
    def prims(self):
        self.costs[self.nodeIndex[self.start]] = 0
        
        for k in range(len(self.visited)):
            print(k)
            cur = self.findMin()
            node1 = self.nodes[cur]
            print(node1.name)
            for l in range(len(node1.adj)):
                new_node = node1.adj[l]
                new_index = self.nodeIndex[new_node.name]
                if(self.visited[new_index] == False and node1.weights[l] < self.costs[new_index]):
                    self.costs[self.nodeIndex[new_node.name]] = node1.weights[l]
                    
            self.visited[cur] = True
            


    def preSwitch(self, node):
        if node.type == 'breaker' or node.type == 'box' or node.type == 'outlet':
            return True
        return False
    def isSwitch(self,node):
        return node.type == "switch"
    def postSwitch(self,node):
        return node.type == "light"

    
    def result(self):
        ret = 0
        for num in self.costs:
            ret+=num
        return ret

check = Wiring()
check.input()
check.prims()
print(check.nodes)
print(check.nodeIndex)
print(check.costs)
print(check.result())
    





