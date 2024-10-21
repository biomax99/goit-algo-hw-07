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

def find_sum(node):
    if node is None:
        return 0
    return node.value + find_sum(node.left) + find_sum(node.right)

# Створення дерева та знаходження суми всіх значень
bst = BinarySearchTree()
values = [20, 10, 30, 5, 15, 25, 35]
for v in values:
    bst.insert(v)

total_sum = find_sum(bst.root)
print(f"Сума всіх значень: {total_sum}")
