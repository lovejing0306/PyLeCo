# coding=utf-8

def main(nums, target):
    dp = [0] * (target + 1)
    dp[0] = 1
    # 动态规划求排列，必须先遍历背包容量，再遍历商品
    for i in range(1, target+1):   # 先遍历背包容量
        sum_ = 0
        for num in nums:   # 再遍历商品
            if num > i:
                continue
            sum_ += dp[i-num]
        dp[i] = sum_
    
    return dp[target]


if __name__ == '__main__':
    target = 4
    nums = [1,2,3]
    res = main(nums, target)
    print(res)
