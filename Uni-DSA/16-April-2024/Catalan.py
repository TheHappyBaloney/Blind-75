'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

# Usage example
tree = BinarySearchTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)
'''
# Factorial Function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Catalan Number Function
def count(n):
    if n == 0:
        return 1
    else:
        cat = factorial(2*n) / (factorial(n+1) * factorial(n))
        return cat

# Usage example
n = 6
print(count(n))