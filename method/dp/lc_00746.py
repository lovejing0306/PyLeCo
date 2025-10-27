# coding=utf-8

from re import L


def main(nums):
    if len(nums)==2:
        return min(nums[0], nums[1])

    dp = [0] * (len(nums)+1)
    for i in range(2, len(dp)):
        dp[i] = min(dp[i-1]+nums[i-1], dp[i-2]+nums[i-2])
    
    return dp[-1]

if __name__ == '__main__':
    cost = [1,100,1,1,1,100,1,1,100,1]
    res = main(cost)
    print(res)
