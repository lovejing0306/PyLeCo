# coding=utf-8

class TreeNode():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


count = 0

def dfs(node):
    """ 
    0: 表示没有被覆盖到
    1: 表示被覆盖到了
    2: 表示安装了摄像头
    """
    global count

    if node is None:  # 如果节点为空，默认表示会被覆盖到
        return 1
    
    l_s = dfs(node.left)
    r_s = dfs(node.right)

    if l_s==2 or r_s==2:  # 如果左右子节点中有任何一个暗装了摄像头，则当前节点肯定会被覆盖到
        return 1
    if l_s == 1 or r_s==1:  # 如果左右子节点中有任何一个没有被覆盖到，则需要在当前节点安装摄像头来覆盖子节点
        count +=1
        return 2
    return 0


def main(root):
    global count
    if root is None:
        count = 0
    elif root.left is None and root.right is None:
        count = 1
    else:
        dfs(root)


if __name__ == '__main__':
    # 测试用例 1: 单个节点
    root1 = TreeNode(0)
    # main(root1)
    # print(count)  # 输出: 1

    # 测试用例 2:
    #     0
    #    / \
    #   0   0
    root2 = TreeNode(0, TreeNode(0), TreeNode(0))
    # main(root2)
    # print(count)  # 输出: 1 (在根节点放摄像头)

    # # 测试用例 3:
    # #       0
    # #      / \
    # #     0   0
    # #    /
    # #   0
    root3 = TreeNode(0, TreeNode(0, TreeNode(0)), TreeNode(0))
    main(root3)
    print(count)  # 输出: 2