# coding=utf-8

def main(prices):
    if len(prices) == 0:
        return 0
    
    dp = []
    for _ in range(len(prices)):
        dp.append([0, 0])
    
    dp[0][0] = -prices[0]
    dp[0][1] = 0

    for i in range(1, len(prices)):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1]-prices[i])   # 这里是和每天只能够执行一次交易的关键区别
        dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
    return dp[len(prices)-1][1]


if __name__ == '__main__':
    prices = [7,1,5,3,6,4]

    res = main(prices)
    print(res)
