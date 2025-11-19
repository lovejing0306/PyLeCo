# coding=utf-8

class TreeNode():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def adjust(node):
    """
    处理删除节点左子树和右子树都存在的情况
    将左子树赋值给右子树的最左节点
    """
    left_node = node.left
    right_node = node.right

    node.left = None

    while right_node.left is not None:
        right_node = right_node.left
    
    right_node.left = left_node
    return node.right


def dfs(node, target):
    if node is None:
        return None
    
    if node.val == target:
        # 分情况讨论
        if node.left is None and node.right is None:
            return None
        elif node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        else:
            return adjust(node)
    
    if node.val < target:
        node.right = dfs(node.right, target)
        return node
    if node.val > target:
        node.left = dfs(node.left, target)
        return node


def main(root, target):
    if root is None:
        return None
    if root.val == target:  # 如果删除的是根节点
        if root.left is None and root.right is None:
            return None
        elif root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            return adjust(root)
    else:
        return dfs(root, target)
