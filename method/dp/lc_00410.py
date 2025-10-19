# coding=utf-8

def main(nums, k):
    """
    更简洁的区间DP版本
    
    状态：dp[i][j][m] = 将区间[i,j]分成m组的最小最大值
    """
    n = len(nums)
    
    # 前缀和
    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1] + num)
    
    # 区间和函数
    def get_sum(i, j):
        return prefix[j + 1] - prefix[i]
    
    # DP数组初始化
    dp = [[[float('inf')] * (k + 1) for _ in range(n)] for _ in range(n)]
    
    # 基础情况：每个区间分成1组
    for i in range(n):
        for j in range(i, n):
            dp[i][j][1] = get_sum(i, j)
    
    # 区间DP主循环
    for gap in range(1, n):                    # 区间长度-1
        for i in range(n - gap):               # 起始位置
            j = i + gap                        # 结束位置
            
            for m in range(2, min(j - i + 2, k + 1)):  # 分组数
                for mid in range(i, j):        # 分割点
                    # [i,mid]分成m-1组 + [mid+1,j]分成1组
                    left = dp[i][mid][m - 1]
                    right = dp[mid + 1][j][1]
                    dp[i][j][m] = min(dp[i][j][m], max(left, right))
    
    return dp[0][n - 1][k]


if __name__ == '__main__':
    nums = [7,2,5,10,8]
    k = 2
    # 只是想出了状态，但是没有实现出来
    print(main(nums, k))