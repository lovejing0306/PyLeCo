# coding=utf-8

def main(nums):
    if len(nums) == 0:
        return 0
    
    dp = [1] * len(nums)

    max_value = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            dp[i] = dp[i-1] + 1
        max_value = max(max_value, dp[i])
    return max_value


if __name__ == '__main__':
    nums = [2,2,2,2,2]
    res = main(nums)
    print(res)
