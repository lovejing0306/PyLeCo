# coding=utf-8

class TreeNode():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_same(node1, node2):
    if node1 is None and node2 is None:
        return True
    if node1 is None and node2 is not None:
        return False
    if node1 is not None and node2 is None:
        return False
    if node1.val != node2.val:
        return False
    
    flag_l = is_same(node1.left, node2.left)
    flag_r = is_same(node1.right, node2.right)
    return flag_l and flag_r

def valid(node1, node2):
    if node2 is None:
        return True
    if node1 is None:
        return False
    flag = False
    if node1.val == node2.val:
        flag = is_same(node1, node2)
    if flag:
        return True
    flag_l = valid(node1.left, node2)
    if flag_l:
        return True
    flag_r = valid(node1.right, node2)
    if flag_r:
        return True
    return False
    
def main(root, sub_root):
    return valid(root, sub_root)


if __name__ == '__main__':
    node0 = TreeNode(0)
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)

    node3.left = node4
    node3.right = node5
    node4.left = node1
    node4.right = node2
    # node2.left = node0

    node11 = TreeNode(1)
    node22 = TreeNode(2)
    node44 = TreeNode(4)

    node44.left = node11
    node44.right = node22

    res = is_same(node4, node44)
    print(res)
    res = main(node3, node4)
    print(res)