# coding=utf-8

class TreeNode():
    def __init__(self, value, left_node=None, right_node=None):
        self.value = value
        self.left_node = left_node
        self.right_node = right_node


def dfs(node, sum_, target):
    if node is None:
        return sum_ == target
    sum_ += node.value
    l = dfs(node.left_node, sum_,  target)
    r = dfs(node.right_node, sum_, target)
    sum_ -= node.value
    return l or r


def main(root, target):
    res = dfs(root, 0, target)
    return res


if __name__ == '__main__':
    root6 = TreeNode(1)
    root6.left_node = TreeNode(2)
    root6.right_node = TreeNode(3)
    root6.left_node.left_node = TreeNode(4)
    root6.right_node.left_node = TreeNode(5)
    root6.right_node.right_node = TreeNode(6)
    root6.left_node.left_node.left_node = TreeNode(7)
    root6.right_node.left_node.right_node = TreeNode(8)

    target = 9

    res = main(root6, target)
    print(res)
