class Node:
    def __init__(self, name, type) -> None:
        self.name = name
        self.type = type
        self.adj = []
        self.weights = []