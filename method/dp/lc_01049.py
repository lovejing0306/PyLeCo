# coding=utf-8

def main(nums):
    """
    思想：设计一种使两堆石头分割后质量最接近的方案
    """
    sum_ = 0
    for num in nums:
        sum_ += num
    
    n = len(nums)
    c = sum_ // 2

    dp = []
    for _ in range(n+1):
        dp.append([0] * (c+1))
    
    for i in range(1, n+1):
        for j in range(1, c+1):
            if nums[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j-nums[i-1]] + nums[i-1], dp[i-1][j])
    return sum_ - 2*dp[n][c]


if __name__ == '__main__':
    stones = [2,7,4,1,8,1]
    res = main(stones)
    print(res)