class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.value:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current.value

# Створення дерева та знаходження мінімального значення
bst = BinarySearchTree()
values = [20, 10, 30, 5, 15, 25, 35]
for v in values:
    bst.insert(v)

min_value = find_min(bst.root)
print(f"Найменше значення: {min_value}")
