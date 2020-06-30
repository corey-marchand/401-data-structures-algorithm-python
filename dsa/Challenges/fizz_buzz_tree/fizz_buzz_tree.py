class Node:
    def __init__(self, left, right, value):
        self.left = left
        self.right = right
        self.value = value

class BinaryTree:
    def __init__(self, root):
        self.root = root

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

    def find_maximum_value(self):
        root_node = self.root

        if not root_node:
            raise ValueError('Empty tree')

        max_value = root_node.value

        def max_recursion(node):
            if not node:
                return

            if node.left:
                if node.left.value > max_value:
                    max_value = node.left.value

                max_recursion(node.left)

            if node.right:
                if node.right.value > max_value:
                    max_value = node.right.value

                max_recursion(node.right)

        max_recursion(root_node)

        return max_value
