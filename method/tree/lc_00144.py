# coding=utf-8

class TreeNode():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(node, nums):
    if node is None:
        return
    nums.append(node.val)
    dfs(node.left, nums)
    dfs(node.right, nums)


def method1(root):
    res = []
    if root is None:
        return res

    stack = [root]
    while len(stack) >0:
        node = stack.pop()
        res.append(node.val)
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
    return res


def method2(root):
    res = []
    dfs(root, res)
    return res


if __name__ == '__main__':
    root6 = TreeNode(1)
    root6.left = TreeNode(2)
    root6.right = TreeNode(3)
    root6.left.left = TreeNode(4)
    root6.right.left = TreeNode(5)
    root6.right.right = TreeNode(6)
    root6.left.left.left = TreeNode(7)
    root6.right.left.right = TreeNode(8)
    
    res1 = method1(root6)
    res2 = method2(root6)
    print(res1)
    print(res2)
    