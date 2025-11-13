# coding=utf-8


class TreeNode():
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def dfs(node, target):
    if node is None:
        return [None, None]
    
    if node.val <= target:  # 需要仔细思考下 ？？？
        left, right = dfs(node.right, target)
        node.right = left
        return [node, right]
    else:
        left, right = dfs(node.left, target)
        node.left = right
        return [left, node]


def main(root, target):
    node1, node2 = dfs(root, target)
    return node1, node2


if __name__ == '__main__':
    node1 = TreeNode(4)
    node2 = TreeNode(2)
    node3 = TreeNode(6)
    node4 = TreeNode(1)
    node5 = TreeNode(3)
    node6 = TreeNode(5)
    node7 = TreeNode(7)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7

    t1, t2 = main(node1, 2)
    print(t1.val, t2.val)