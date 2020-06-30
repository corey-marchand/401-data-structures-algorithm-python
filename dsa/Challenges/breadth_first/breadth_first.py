class Node(object):
    def __init__(self, name):
        self.name = name
        self.adjacencyList = []
        self.visited = False
        self.precdecessor = None

def breadth_first_search(startNode):
    queue = []
    queue.append(startNode)
    startNode.visited = True

    while queue:
        actualNode = queue.pop(0)

        for n in actualNode.adjacencyList:
            if not n.visited:
                n.visited = True
                queue.append(n)

node1 = Node("a")
node2 = Node("b")
node3 = Node("c")
node4 = Node("d")
node5 = Node("e")

node1.adjacencyList.append(node2)
node1.adjacencyList.append(node3)
node1.adjacencyList.append(node4)
node1.adjacencyList.append(node5)

bfs = breadth_first_search(node1)
breadth_first_search.bfs(node1)
