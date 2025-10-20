# coding=utf-8

class TreeNode():
    def __init__(self, value, left_node=None, right_node=None):
        self.value = value
        self.left_node = left_node
        self.right_node = right_node


def dfs1(node, depth, depths):
    if node.left_node is None and node.right_node is None:
        depths.append(depth)
        return
    if node.left_node is not None:
        dfs1(node.left_node, depth+1, depths)
    if node.right_node is not None:
        dfs1(node.right_node, depth+1, depths)


def method1(root):
    depths = []
    dfs1(root, 1, depths)
    return max(depths)


def dfs2(node):
    if node is None:
        return 0
    left_d = dfs2(node.left_node)
    right_d = dfs2(node.right_node)
    d = max(left_d, right_d) + 1
    return d


def method2(root):
    return dfs2(root)


if __name__ == '__main__':
    root6 = TreeNode(1)
    root6.left_node = TreeNode(2)
    root6.right_node = TreeNode(3)
    root6.left_node.left_node = TreeNode(4)
    root6.right_node.left_node = TreeNode(5)
    root6.right_node.right_node = TreeNode(6)
    root6.left_node.left_node.left_node = TreeNode(7)
    root6.right_node.left_node.right_node = TreeNode(8)
    root6.right_node.left_node.right_node.left_node = TreeNode(9)

    print(method1(root6))
    print(method2(root6))