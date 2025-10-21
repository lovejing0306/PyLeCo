# coding=utf-8

class TreeNode():
    def __init__(self, value, left_node=None, right_node=None):
        self.value = value
        self.left_node = left_node
        self.right_node = right_node


def dfs(node1, node2):
    if node1 is None and node2 is None:
        return None

    if node1 is None:   # 如果第一个节点为 空，直接返回第二个节点
        return node2
    if node2 is None:   # 如果第二个节点为 空，直接返回第一个节点
        return node1

    l = dfs(node1.left_node, node2.left_node)
    r = dfs(node1.right_node, node2.right_node)

    node = TreeNode(node1.value + node2.value, l, r)
    return node
    

def main(root1, root2):
    return dfs(root1, root2)


def print_tree(root):
    """前序遍历打印树中所有元素"""
    if root is None:
        return
    
    print(root.value, end=' ')
    print_tree(root.left_node)
    print_tree(root.right_node)

if __name__ == '__main__':
    root1 = TreeNode(1)
    root1.left_node = TreeNode(3)
    root1.right_node = TreeNode(2)
    
    root2 = TreeNode(2)
    root2.left_node = TreeNode(1)
    root2.right_node = TreeNode(3)

    print("合并前的树1: ", end='')
    print_tree(root1)
    print()
    
    print("合并前的树2: ", end='')
    print_tree(root2)
    print()
    
    root = main(root1, root2)
    print("合并后的树: ", end='')
    print_tree(root)
    print()
