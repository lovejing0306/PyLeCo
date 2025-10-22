# coding=utf-8

class TreeNode():
    def __init__(self, value, left_node=None, right_node=None):
        self.value = value
        self.left_node = left_node
        self.right_node = right_node


def dfs(node, values):
    if node is None:
        return 
    dfs(node.left_node, values)
    if node.value in values:
        values[node.value]+=1
    else:
        values[node.value]=1
    dfs(node.right_node, values)


def main(root):
    """
    naive 方案实现
    """

    values = {}
    dfs(root, values)
    print(values)
    max_num = 0
    for key, value in values.items():
        max_num = max(max_num, value)

    res = []
    for key, value in values.items():
        if value == max_num:
            res.append(key)
    return res


if __name__ == '__main__':
    root1 = TreeNode(1)
    root2 = TreeNode(2)
    root3 = TreeNode(3)
    root4 = TreeNode(2)

    root1.right_node = root2
    root2.left_node = root4
    root2.right_node = root3

    res = main(root1)
    print(res)
