# coding=utf-8

from re import L


class TreeNode():
    def __init__(self, value, left_node=None, right_node=None):
        self.value = value
        self.left_node = left_node
        self.right_node = right_node


def dfs(node, node1, node2):
    if node is None:
        return None
    
    if node1.value <= node.value <= node2.value:
        return node
    if node2.value <= node.value <= node1.value:
        return node
    
    L = dfs(node.left_node, node1, node2)
    if L is not None:
        return L
    R = dfs(node.right_node, node1, node2)
    if R is not None:
        return R
    return None


def main(root, node1, node2):
    return dfs(root, node1, node2)

if __name__ == '__main__':
    root1 = TreeNode(1)
    root2 = TreeNode(2)
    root3 = TreeNode(3)
    root4 = TreeNode(4)

    root1.right_node = root2
    root2.right_node = root3
    root3.right_node = root4

    node = main(root1, root3, root4)
    print(node.value)