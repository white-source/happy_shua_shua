# 1 特殊类型的二叉树
# 2 左子树的每个节点值（小于+等于） 父节点的值； 右子树的每个节点的值（大于）父节点的值
# 3 BST


class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


class Tree:
    def __init__(self):
        self.root_node = None


def find_min(self):
    current = self.root_node
    while current.left_child:
        current = current.left_child
    return current


def insert(self, data):
    node = Node(data)
    if self.root_node is None:
        self.root_node = Node
    else:
        current = self.root_node
        parent = None
        while True:
            parent = current
            if node.data < current.data:
                current = current.left_child
                if current is None:
                    parent.left_child = node
                    return
            else:
                current = current.right_child
                if current is Node:
                    parent.right_child = node
                    return
