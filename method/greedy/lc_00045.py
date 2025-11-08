# coding=utf-8
import sys


def main(nums):
    jumps = 0
    cur_end = 0   # 当前跳跃结束点位置
    farthest = 0  # 下一次跳跃能够到达的最远位置

    for i in range(0, len(nums)-1):
        farthest = max(farthest, nums[i] + i)
        if i == cur_end:  # 如果 i 到达当前结束点
            jumps += 1
            cur_end = farthest
            if cur_end >=len(nums)-1:
                break
    return jumps


def method2(nums):
    if len(nums) == 1:
        return 0

    dp = [sys.maxsize] * len(nums)
    dp[0] = 0


    for i in range(1, len(nums)):
        j = i-1
        while j>=0:
            if nums[j] + j >= i:
                dp[i] = min(dp[i], dp[j] + 1)
            j-=1
    return dp[len(nums)-1]


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    res = method2(nums)
    print(res)
