# coding=utf-8

class TreeNode():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs(node, target):
    if node is None:
        return TreeNode(target)
    if node.val < target:
        node.right = dfs(node.right, target)
    elif node.val > target:
        node.left = dfs(node.left, target)
    return node
    

def main(root, target):
    return dfs(root, target)

