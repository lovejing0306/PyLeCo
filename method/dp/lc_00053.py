# coding=utf-8

def main(nums):
    dp = [0] * len(nums)
    dp[0] = nums[0]  
    max_value = nums[0]

    for i in range(1, len(nums)):
        dp[i] = max(dp[i-1]+nums[i], nums[i])  # 获取在当前坐标下的最大值
        max_value = max(dp[i], max_value)    # 记录全局最大值
    return max_value


if __name__ == '__main__':
    nums = [5,4,-1,7,8]
    res = main(nums)
    print(res)