# coding=utf-8

def main(n):
    dp = [0] * (n+1)
    dp[0] = 1

    for i in range(1, n+1):  # 遍历节点数
        for j in range(1, i+1):
            l = j-1  # 以 j 为根节点时，左边节点的数量
            r = i-j  # 以 j 为根节点时，右边节点的数量
            dp[i] +=(dp[l] * dp[r])  # 以 j 为根节点时，可以构成的二叉搜索树的数量
    return dp[-1]

if __name__ == '__main__':
    res = main(4)
    print(res)