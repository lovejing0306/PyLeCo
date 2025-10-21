# coding=utf-8
import copy


class TreeNode():
    def __init__(self, value, left_node=None, right_node=None):
        self.value = value
        self.left_node = left_node
        self.right_node = right_node


def dfs(node, target, sum_, path, paths):
    if node.left_node is None and node.right_node is None:
        path.append(node.value)
        sum_ += node.value
        print(sum_)
        if sum_ == target:
            paths.append(copy.deepcopy(path))
        path.pop()
        return 
    sum_ += node.value
    path.append(node.value)
    if node.left_node is not None:
        dfs(node.left_node, target, sum_, path, paths)
    if node.right_node is not None:
        dfs(node.right_node, target, sum_, path, paths)
    path.pop()


def main(root, target):
    if root is None:
        return root
    paths = []
    path = []

    dfs(root, target, 0, path, paths)

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

    target = 10

    paths = main(root6, target)
    print(paths)