# coding=utf-8

class TreeNode():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def dfs(node):
    if node is None:
        return [0, 0]  # [不偷当前节点, 偷当前节点]
    
    res_l = dfs(node.left)
    res_r = dfs(node.right)
    # 不偷当前节点：子节点可偷可不偷 !!!
    value_0 = max(res_l) + max(res_r)
    value_1 = res_l[0] + res_r[0] + node.value

    del res_l
    del res_r
    return [value_0, value_1]


def main(root):
    res = dfs(root)
    return max(res)


if __name__ == '__main__':
    node1 = TreeNode(3)
    node20 = TreeNode(4)
    node21 = TreeNode(5)
    node30 = TreeNode(1)
    node31 = TreeNode(3)
    node32 = TreeNode(1)

    node1.left = node20
    node1.right = node21

    node20.left = node30
    node20.right = node31

    node21.right = node32

    res = main(node1)
    print(res)