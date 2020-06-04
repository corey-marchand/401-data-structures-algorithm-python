class BinaryTree:
    def __init__(self, root):
        self.root = root

class Node:
    def __init__(self, left, right, value):
        self.left = left
        self.right = right
        self.value = value

    def FizzBuzzTree(self, tree):
        node = self.value
        if node == None:
            print('Does not exist')
        elif node % 3 == 0 and node % 5 == 0:
            node == 'fizzbuzz'
        elif node % 3 == 0:
            node == 'fizz'
        elif node % 5 == 0:
            node == 'buzz'

    def findMaximumValue(self):
        node = BinaryTree.root
        max_node = []


        if node == None:
            return 'tree does not exist'

        if node.left:
            if node.left >= node
                max_node = node.left
            elif node >= node.left
                max_node = node
        if node.right:
            if node.right >= node
                max_node = node.right
            elif node >= node.right
                max_node = node
        return max_node:

        findMaximumValue(node.left)
        findMaximumValue(node.right)




