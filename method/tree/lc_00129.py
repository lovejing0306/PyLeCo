# coding=utf-8

class TreeNode():
    def __init__(self, value, left_node=None, right_node=None):
        self.value = value
        self.left_node = left_node
        self.right_node = right_node


def dfs(node, sum_, nums):
    sum_ = sum_ * 10 + node.value
    if node.left_node is None and node.right_node is None:  # 此时为 叶子节点
        nums.append(sum_)
        return 
    
    if node.left_node is not None:  # 如果 左子树 不为空，则访问左子树
        dfs(node.left_node, sum_, nums)
    if node.right_node is not None:  # 如果 右子树 不为空，则访问右子树
        dfs(node.right_node, sum_, nums)
    

def main(root):
    if root is None:
        return 0
    nums = []
    dfs(root, 0, nums)   # 初始状态下，sum 为 0

    return sum(nums)


if __name__ == '__main__':
    # 测试用例1: 原始测试数据
    print("=== 测试用例1: 基本二叉树 ===")
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    node3 = TreeNode(0)
    node4 = TreeNode(1, node1, node2)
    node5 = TreeNode(4, node4, node3)

    res = main(node4)
    print(f"树结构: 1->2, 1->3, 结果: {res}")
    
    # 测试用例2: LeetCode官方示例
    print("\n=== 测试用例2: LeetCode官方示例 ===")
    # 树结构:     4
    #           / \
    #          9   0
    #         / \
    #        5   1
    root2 = TreeNode(4)
    root2.left_node = TreeNode(9)
    root2.right_node = TreeNode(0)
    root2.left_node.left_node = TreeNode(5)
    root2.left_node.right_node = TreeNode(1)
    
    res2 = main(root2)
    print(f"树结构: 4->9->5, 4->9->1, 4->0, 结果: {res2}")
    
    # 测试用例3: 单节点
    print("\n=== 测试用例3: 单节点 ===")
    root3 = TreeNode(5)
    res3 = main(root3)
    print(f"树结构: 5, 结果: {res3}")
    
    # 测试用例4: 只有左子树
    print("\n=== 测试用例4: 只有左子树 ===")
    root4 = TreeNode(1)
    root4.left_node = TreeNode(2)
    root4.left_node.left_node = TreeNode(3)
    res4 = main(root4)
    print(f"树结构: 1->2->3, 结果: {res4}")
    
    # 测试用例5: 包含0值节点
    print("\n=== 测试用例5: 包含0值节点 ===")
    root5 = TreeNode(1)
    root5.left_node = TreeNode(0)
    root5.right_node = TreeNode(1)
    root5.left_node.left_node = TreeNode(0)
    root5.left_node.right_node = TreeNode(1)
    root5.right_node.right_node = TreeNode(0)
    res5 = main(root5)
    print(f"树结构: 包含多个0值节点, 结果: {res5}")
    
    # 测试用例6: 复杂树结构
    print("\n=== 测试用例6: 复杂树结构 ===")
    root6 = TreeNode(1)
    root6.left_node = TreeNode(2)
    root6.right_node = TreeNode(3)
    root6.left_node.left_node = TreeNode(4)
    root6.right_node.left_node = TreeNode(5)
    root6.right_node.right_node = TreeNode(6)
    root6.left_node.left_node.left_node = TreeNode(7)
    root6.right_node.left_node.right_node = TreeNode(8)
    res6 = main(root6)
    print(f"树结构: 复杂不规则树, 结果: {res6}")
    
    # 测试用例7: 空树
    print("\n=== 测试用例7: 空树 ===")
    res7 = main(None)
    print(f"树结构: 空树, 结果: {res7}")
    
    # 测试用例8: 较大数字
    print("\n=== 测试用例8: 较大数字 ===")
    root8 = TreeNode(9)
    root8.left_node = TreeNode(9)
    root8.right_node = TreeNode(9)
    root8.left_node.left_node = TreeNode(9)
    root8.right_node.right_node = TreeNode(9)
    res8 = main(root8)
    print(f"树结构: 999, 999, 结果: {res8}")
    
    print("\n=== 所有测试完成 ===")
    print(f"测试用例总数: 8个")