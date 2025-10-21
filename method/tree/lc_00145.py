# coding=utf-8

class TreeNode():
    def __init__(self, value, left_node=None, right_node=None):
        self.value =value
        self.left_node = left_node
        self.right_node = right_node


def dfs(node, nums):
    if node is None:
        return
    dfs(node.left_node, nums)
    dfs(node.right_node, nums)
    nums.append(node.value)


def method2(root):
    res = []
    if root is None:
        return res
    dfs(root, res)
    return res


def method1(root):
    """
    前序遍历：中左右
    后序遍历：左右中，可以看作 中左右->右左中->左右中
    """
    res = []
    if root is None:
        return res

    stack = [root]

    while len(stack) > 0:
        node = stack.pop()
        res.append(node.value)
        if node.left_node is not None:
            stack.append(node.left_node)
        if node.right_node is not None:
            stack.append(node.right_node)

    res.reverse()
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
    
    res1 = method1(root6)
    res2 = method2(root6)
    print(res1)
    print(res2)
