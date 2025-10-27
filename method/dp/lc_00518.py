# coding=utf-8

def main(amount, coins):
    dp = [0] * (amount+1)
    dp[0] = 1
    
    # 这是组合问题，不能含有重复的元素，所以要先遍历 物品，再遍历 面值
    for i in range(len(coins)):  # 先遍历物品
        for j in range(coins[i], amount + 1):   # 再遍历面值
            dp[j] += dp[j-coins[i]]  # 面值 j 由前 i 个硬币组合的方式
    return dp[amount]


if __name__ == '__main__':
    amount = 5
    coins = [1, 2, 5]
    res = main(amount, coins)
    print(res)