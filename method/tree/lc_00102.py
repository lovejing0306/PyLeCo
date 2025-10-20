# coding=utf-8

import queue

class TreeNode():
    def __init__(self, value, left_node=None, right_node=None):
        self.value = value
        self.left_node = None
        self.right_node = None


def main(root):
    nums = []
    if root is None:
        return nums

    qq = queue.Queue()
    qq.put(root)

    while qq.qsize() > 0:
        nums_ = []
        for _ in range(qq.qsize()):
            node = qq.get()
            nums_.append(node.value)
            if node.left_node is not None:
                qq.put(node.left_node)
            if node.right_node is not None:
                qq.put(node.right_node)
        nums.append(nums_)

    return nums


if __name__ == '__main__':
    root6 = TreeNode(1)
    root6.left_node = TreeNode(2)
    root6.right_node = TreeNode(3)
    root6.left_node.left_node = TreeNode(4)
    root6.right_node.left_node = TreeNode(5)
    root6.right_node.right_node = TreeNode(6)
    root6.left_node.left_node.left_node = TreeNode(7)
    root6.right_node.left_node.right_node = TreeNode(8)

    print(main(root6))