class Node:
    def __init__(self, data):
        self.vertex = data
        self.next = None

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [None] * self.vertices

    def add_edge(self, src, dest):
        node = Node(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        node = Node(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def addNode():
        pass

    def getNodes():

    def getNeighbors():
        pass

    def size():
        pass
