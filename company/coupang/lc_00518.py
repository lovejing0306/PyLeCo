# coding=utf-8

def main(coins, amount):
    dp = [0] * (amount+1)  # 状态为：当前币值下，由不同零钱组成的兑换方式
    dp[0] = 1
 
    for coin in coins:  # 由于求解的是组合，所以必须先遍历币种
        for i in range(1, amount +1):
            if coin > i:
                dp[i] = dp[i]
            else:
                dp[i] = dp[i] + dp[i-coin]
    return dp[-1]


if __name__ == '__main__':
    amount = 5
    coins = [1, 2, 5]

    res = main(coins, amount)
    print(res)
