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

        print(node)

        FizzBuzzTree(self.left)
        FizzBuzzTree(self.right)

