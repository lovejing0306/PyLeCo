# coding=utf-8

def main(nums):
    dp = []
    for _ in range(len(nums)):
        dp.append([0] * 5)

    dp[0][1] = -nums[0]
    dp[0][3] = -nums[0]

    for i in range(1, len(nums)):
        dp[i][0] = 0
        dp[i][1] = max(dp[i-1][1], dp[i-1][0]-nums[i])
        dp[i][2] = max(dp[i-1][2], dp[i-1][1]+nums[i])
        dp[i][3] = max(dp[i-1][3], dp[i-1][2]-nums[i])
        dp[i][4] = max(dp[i-1][4], dp[i-1][3]+nums[i])
    
    return dp[-1][-1]

if __name__ == '__main__':
    nums = [3,3,5,0,0,3,1,4]
    res = main(nums)
    print(res)