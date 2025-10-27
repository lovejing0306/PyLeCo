# coding=utf-8

import sys


def main(coins, amount):
    dp = [sys.maxsize] * (amount + 1)

    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin > i:
                continue
            dp[i] = min(dp[i], dp[i-coin]) + 1
    
    if dp[amount] < sys.maxsize:
        return dp[amount]
    else:
        return -1


if __name__ == '__main__':
    amount = 3
    coins = [2]
    res = main(coins, amount)
    print(res)

