# coding=utf-8

class TreeNode():
    def __init__(self, value, left_node=None, right_node=None):
        self.value = value
        self.left_node = left_node
        self.right_node = right_node

# 和标准答案实现有差异
def dfs(node, nums):
    if node is None:
        return 0
    
    l = dfs(node.left_node, nums)  # 左子树的最优单路径
    r = dfs(node.right_node, nums)  # 右子树的最优单路径
    # 计算在当前节点的最优路径
    m1 = l + r + node.value  # 情况1
    m2 = l + node.value  # 情况2
    m3 = r + node.value  # 情况3
    m4 = node.value # 情况4:只有当前节点
    nums.append(max([m1, m2, m3, m4]))  # 选择最大的值
    # 计算在节点的最优单边路径
    m = max(l, r)
    m = max(m+node.value, node.value)
    return m

def main(root):
    nums = []  # 记录在每个节点的最优值
    dfs(root, nums)
    return max(nums)

if __name__ == '__main__':
    # root6 = TreeNode(4)
    # root6.left_node = TreeNode(9)
    # root6.right_node = TreeNode(0)
    # root6.left_node.left_node = TreeNode(5)
    # root6.left_node.right_node = TreeNode(1)

    root6 = TreeNode(-10)
    root6.left_node = TreeNode(9)
    root6.right_node = TreeNode(20)
    root6.right_node.left_node = TreeNode(15)
    root6.right_node.right_node = TreeNode(7)

    print(main(root6))
