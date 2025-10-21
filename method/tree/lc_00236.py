# coding=utf-8

class TreeNode():
    def __init__(self, value, left_node=None, right_node=None):
        self.value = value
        self.left_node = left_node
        self.right_node = right_node


def dfs(node, node1, node2):
    if node is None:
        return 0, None

    num1, target_node1 = dfs(node.left_node, node1, node2)
    if num1 == 2:
        return target_node1
    num2, target_node2 = dfs(node.right_node, node1, node2)
    if num2 == 2:
        return target_node2

    num = num1 + num2
    if num == 2:
        return num, node
    if node is  node1:
        return 1 + num, None
    if node is  node2:
        return 1 + num, None
    return num, None


def main(root, node1, node2):
    num, node = dfs(root, node1, node2)
    return node


if __name__ == '__main__':
    root1 = TreeNode(1)
    root2 = TreeNode(2)
    root3 = TreeNode(3)
    root4 = TreeNode(4)

    root1.left_node = root2
    root1.right_node = root3
    root3.left_node = root4
    

    node = main(root1, root2, root4)
    print(node.value)