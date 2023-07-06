from collections import defaultdict

class Node:
    def __init__(self, name):
        self.name = name
        self.whichSwitch = ""
        self.edges = defaultdict(list) 
        self.ID = ""