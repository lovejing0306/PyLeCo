# coding=utf-8

class TreeNode():
    def __init__(self, value, left_node=None, right_node=None):
        self.value = value
        self.left_node = left_node
        self.right_node = right_node


def dfs(node1, node2):
    # 想清楚边界条件
    if node1 is None and node2 is None: # 只有两个节点都为 None 时，才返回 true
        return True
    if node1 is not None and node2 is None:  # 其中一个节点为 None 是 False
        return False 
    if node1 is None and node2 is not None:   # 其中一个节点都为 None 是 False
        return False
    if node1.value != node2.value:  # 如果不为 None，但值不相等，也为 False
        return False
    
    l = dfs(node1.left_node, node2.right_node)
    r = dfs(node1.right_node, node2.left_node)
    return l and r


def main(root):
    return dfs(root, root)


if __name__ == '__main__':
    root6 = TreeNode(1)
    root6.left_node = TreeNode(2)
    root6.right_node = TreeNode(2)
    root6.left_node.left_node = TreeNode(3)
    root6.right_node.right_node = TreeNode(4)

    print(main(root6))
