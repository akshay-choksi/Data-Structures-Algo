'''
Akshay Choksi (ajc9yr)
Collaborated with Ethan Tran (ett6xuq)
- Discussed idea of implementing a dict for queue 
- Discussed how to implement Prim's seperately for each "tree" (pre -> post)
'''
from collections import defaultdict
import math
from node import *


class Connection:
    def __init__(self, count, breakerBox):
        self.junctions = defaultdict
        self.adj = defaultdict(list)
        self.adjJBO = defaultdict(list)
        self.J = count
        # Breaker does not always == b1
        self.breaker_box = breakerBox
        self.switchlist = []
    
    #Helper methods for connection method (suggested by TA Ethan to cut down on if statements)
    def preSwitch(self,node):
        if node.ID == 'breaker' or node.ID == 'box' or node.ID == 'outlet':
            return True
        return False

    def isSwitch(self,node):
        return node.ID == "switch"
    
    def postSwitch(self,node):
        return node.ID == "light"
    
    #breaker,outler,box
    def isconnected_pre(self,n1,n2):
        return self.preSwitch(n1) == True and self.preSwitch(n2) == True
    
    #light to light or swithc
    def isconnected_post(self,n1,n2):
        if (self.postSwitch(n1) == True and self.postSwitch(n2) == True and self.whichSwitch == self.whichSwitch):
            return True
        elif self.isSwitch(n1) == True and self.postSwitch(n2) == True and (n2.whichSwitch == n1.name or n1.whichSwitch == n2.name):
           return True
        else:
            return False
    #for use in prim to run twice
    def isconnected_last(self, n1, n2):
        return (self.preSwitch(n1) == True and self.isSwitch(n2) == True) or (self.preSwitch(n2) == True and self.isSwitch(n1) == True)

    #Add both possible connections
    def add_edge(self, n1, n2, weight):
        #Valid connections (could save time later)
        if self.isconnected_pre(n1, n2) or self.isconnected_post(n1, n2) or self.isconnected_last(n1, n2):
            self.adj[n1].append([n2, weight])
        if self.isconnected_pre(n2, n1) or self.isconnected_post(n2, n1) or self.isconnected_last(n2, n1):
            self.adj[n2].append([n1, weight])

    def prim(self):
        pq = {self.breaker_box : 0}
        visited = []
        done = []
        total_cost = 0

        while pq:
            node = min(pq, key =pq.get)
            cost = pq[node]

            del pq[node]
            done.append(node)
            visited.append(node)
            total_cost += cost

            for neighbors in self.adj[node]:
                adjNeighbor = neighbors[0]
                adjcost = neighbors[1]
                if self.isconnected_pre(node, adjNeighbor) == True:
                    if adjNeighbor not in visited:
                        pq[adjNeighbor] = adjcost
                        visited.append(adjNeighbor)
                    elif adjNeighbor not in done and adjNeighbor in visited: 
                        if adjcost < pq[adjNeighbor]:
                            pq[adjNeighbor] = adjcost
                else:
                    pass
     
        for switches in self.switchlist:
            if len(self.switchlist) != 0:
                start_cost = math.inf
            for neighbors in self.adj[switches]:
                adjNeighbor = neighbors[0]
                adjcost = neighbors[1]
                if self.isconnected_last(switches, adjNeighbor) == True:
                    if start_cost > adjcost:
                        start_cost = adjcost
 
            total_cost += start_cost
            pq_post = {switches : 0}
            while pq_post:
                node = min(pq_post, key =pq_post.get)
                cost = pq_post[node]

                del pq_post[node]
                done.append(node)
                visited.append(node)
                total_cost += cost

                for neighbors in self.adj[node]:
                    adjNeighbor = neighbors[0]
                    adjcost = neighbors[1]

                    if self.isconnected_post(node, adjNeighbor) == True:
                        if adjNeighbor not in visited:
                            pq_post[adjNeighbor] = adjcost
                            visited.append(adjNeighbor)
                        elif adjNeighbor not in done and adjNeighbor in visited: 
                            if adjcost < pq_post[adjNeighbor]:
                                pq_post[adjNeighbor] = adjcost
                else:
                    pass

        return total_cost
    
    
