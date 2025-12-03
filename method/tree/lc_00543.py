# coding=utf-8

class TreeNode():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def main(root):
    max_v = 0
    def temp(node):
        nonlocal max_v
        if node is None:
            return 0
        l = temp(node.left)
        r = temp(node.right)

        max_v = max(max_v, l+r)
        return max(l, r) + 1
    temp(root)
    return max_v

if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5

    main(node1)