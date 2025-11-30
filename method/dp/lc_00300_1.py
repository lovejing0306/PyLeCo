# coding=utf-8

def main(nums):
    if nums is None or len(nums) == 0:
        return 0

    res = 0
    dp = [1] * len(nums)

    for i in range(len(nums)):
        j = i-1
        max_v = 0
        while j>=0:
            if nums[i] > nums[j]:
                max_v = max(dp[j], max_v)
            j-=1
        dp[i] = max_v + 1  # 以当前元素为节点的最长递增子序列
        res = max(res, dp[i])
    return res


if __name__ == '__main__':
    nums = [0,1,0,3,2,3]

    res = main(nums)
    print(res)