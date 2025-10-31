# coding=utf-8

def main(nums):
    if len(nums) == 0:
        return 0

    dp = [0]*len(nums)
    dp[0] = 1

    for i in range(1, len(nums)):
        j = i-1
        max_value = 0
        while j>=0:
            if nums[i] > nums[j]:
                max_value = max(dp[j], max_value)
            j-=1
        dp[i] = max_value + 1

    return dp[len(nums)-1]


if __name__ == '__main__':
    nums = [0,1,0,3,2,3]
    res = main(nums)
    print(res)