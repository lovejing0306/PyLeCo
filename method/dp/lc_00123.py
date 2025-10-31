# coding=utf-8

def main(prices):
    if len(prices) == 0:
        return 0
    
    dp = []
    for _ in range(len(prices)):
        dp.append([0] * 5)
    
    dp[0][0] = 0    # 第 0 天没有执行交易
    dp[0][1] = -prices[0]   # 第 0 天第一次持有股票
    dp[0][2] = 0            # 第 0 天第一次没持有股票
    dp[0][3] = -prices[0]   # 第 0 天第二次持有股票
    dp[0][4] = 0            # 第 0 天第二次没持有股票

    for i in range(1, len(prices)):
        # dp[i][0] = dp[i-1][0]  # 该状态永远等于 0，由于永远没有执行交易
        dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        dp[i][2] = max(dp[i-1][2], dp[i-1][1] + prices[i])
        dp[i][3] = max(dp[i-1][3], dp[i-1][2] - prices[i])
        dp[i][4] = max(dp[i-1][4], dp[i-1][3] + prices[i])
    return dp[len(prices)-1][4]


if __name__ == '__main__':
    prices = [3,3,5,0,0,3,1,4]
    # prices = [1,2,3,4,5]
    # prices = [7,6,4,3,1] 
    res = main(prices)
    print(res)
