# coding=utf-8

import sys

def main(nums, m):
    """
    动态规划，不是最优方案。在该题目中提交后会出超时问题
    """
    dp = []
    for _ in range(m + 1):
        dp.append([0] * len(nums))
    
    sum_ = 0
    for i, num in enumerate(nums):
        sum_ += num
        dp[1][i] = sum_
    
    for i in range(2, m+1):
        for j in range(i-1, len(nums)):
            min_val = sys.maxsize
            a = 0
            for k in range(j, i-2, -1):  # 不包括 i-2
                a += nums[k]
                max_val = max(dp[i-1][k-1], a)  # 先取最大
                min_val = min(min_val, max_val)  # 然后从最大里面取最小
                k-=1
            dp[i][j] = min_val

    return dp[-1][-1]


if __name__ == '__main__':
    # weights = [1,2,3,4,5,6,7,8,9,10]
    # D = 5

    # weights = [3,2,2,4,1,4]
    # D = 3

    weights = [1,2,3,1,1]
    D = 4

    res = main(weights, D)
    print(res)