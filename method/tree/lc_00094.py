# coding=utf-8

class TreeNode():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(node, nums):
    if node is None:
        return
    dfs(node.left, nums)
    nums.append(node.val)
    dfs(node.right, nums)


def method2(root):
    res = []
    dfs(root, res)
    return res


def method1(root):
    res = []
    if root is None:
        return res
    
    stack = []
    cur = root   # 需要一个临时指针，指向当前变量
    while cur is not None or len(stack) >0:  # 双条件判断 当前节点不空 或 栈的元素个数大于 0
        if cur is not None:  # 如果当前节点不为 空
            stack.append(cur)  # 只负责入栈
            cur = cur.left   # 取当前节点的 左节点
        else:  # 如果当前节点为 空
            cur = stack.pop()  # 只负责出栈
            res.append(cur.val)
            cur = cur.right  # 取当前节点的 右节点
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