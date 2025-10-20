# coding=utf-8
import queue

class TreeNode():
    def __init__(self, value, left_node=None, right_node=None):
        self.value = value
        self.left_node = left_node
        self.right_node = right_node


def main(root):
    if root is None:
        return 0

    qq = queue.Queue()
    
    qq.put(root)

    count = 0
    while qq.qsize()>0:
        for _ in range(qq.qsize()):
            node = qq.get()
            if node.left_node is not None:
                qq.put(node.left_node)
            if node.right_node is not None:
                qq.put(node.right_node)
        count += 1
    return count

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
