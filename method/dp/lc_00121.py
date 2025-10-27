# coding=utf-8


def main(prices):
    """ 
    股票交易最核心的问题是持有和不持有状态下，手里具有现金数
    """
    dp = [[0, 0] for _ in range(len(prices))]

    dp[0][0] = -prices[0]

    for i in range(1, len(prices)):
        dp[i][0] = max(dp[i-1][0], -prices[i])
        dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
    
    return dp[len(prices)-1][-1]


if __name__ == '__main__':
    pp = [7,1,5,3,6,4]
    res = main(pp)
    print(res)