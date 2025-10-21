# coding=utf-8

class TreeNode():
    def __init__(self, value, left_node=None, right_node=None):
        self.value = value
        self.left_node = left_node
        self.right_node = right_node


def dfs(node, nums):
    if node is None:
        return
    dfs(node.left_node, nums)
    nums.append(node.value)
    dfs(node.right_node, nums)


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
            cur = cur.left_node   # 取当前节点的 左节点
        else:  # 如果当前节点为 空
            cur = stack.pop()  # 只负责出栈
            res.append(cur.value)
            cur = cur.right_node  # 取当前节点的 右节点
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