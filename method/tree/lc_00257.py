# coding=utf-8
import copy

class TreeNode():
    def __init__(self, value, left_node=None, right_node=None):
        self.value = value
        self.left_node = left_node
        self.right_node = right_node


def dfs(node, path, paths):
    if node.left_node is None and node.right_node is None:
        path.append(node.value)
        paths.append(copy.deepcopy(path))
        path.pop()
        return
    path.append(node.value)
    if node.left_node is not None:
        dfs(node.left_node, path, paths)
    if node.right_node is not None:
        dfs(node.right_node, path, paths)
    path.pop()


def main(root):
    if root is None:
        return []
    
    paths = []
    path = []

    dfs(root, path, paths)
    return paths


if __name__ == '__main__':
    root6 = TreeNode(1)
    root6.left_node = TreeNode(2)
    root6.right_node = TreeNode(3)
    root6.left_node.left_node = TreeNode(4)
    root6.right_node.left_node = TreeNode(5)
    root6.right_node.right_node = TreeNode(6)
    root6.left_node.left_node.left_node = TreeNode(7)
    root6.right_node.left_node.right_node = TreeNode(8)

    paths = main(root6)
    print(paths)