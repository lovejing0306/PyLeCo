# coding=utf-8
import sys

def main(nums, m):
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
    nums = [7,2,5,10,8]
    m = 2

    res = main(nums, m)
    print(res)