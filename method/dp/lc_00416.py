# coding=utf-8

def main(nums):
    if len(nums) < 2:
        return False
    
    sum = 0
    for num in nums:
        sum+=num
    
    if sum % 2 !=0:
        return False
    
    c = sum // 2
    n = len(nums)

    dp = []
    for _ in range(n+1):
        dp.append([0] * (c+1))
    
    for i in range(1, n+1):
        for j in range(1, c+1):
            if nums[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j-nums[i-1]] + nums[i-1], dp[i-1][j])

    return dp[n][c] == c 


if __name__ == '__main__':
    nums = [1,5,11,5, 6]
    res = main(nums)
    print(res)