# coding=utf-8

def main(prices, k):
    """
    关键点：更开始，钱袋初始化为 0，如果买入，则从钱袋中减钱；如果卖出，则给钱袋加钱
    """
    if prices is None or len(prices) ==  0:
        return 0
    
    if k <= 0:
        return 0
    
    n = len(prices)

    # 如果 k >= n//2，相当于可以进行无限次交易
    # 因为最多只能进行 n//2 次有效交易（每次交易需要买入和卖出）
    if k>=n // 2:  
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:  # 贪心算法：只要明天价格比今天高就买入
                profit += prices[i]-prices[i-1]
        return profit
    
    # dp[i][j][0] 表示第i天，已完成j次交易，当前不持有股票的最大利润
    # dp[i][j][1] 表示第i天，已完成j次交易，当前持有股票的最大利润
    # 注意：这里完成一次交易指的是买入并卖出
    # 初始化dp数组
    dp = [[[0, 0] for _ in range(k + 1)] for _ in range(n)]
    
    # 初始状态
    for j in range(k + 1):
        dp[0][j][0] = 0  # 第0天不持有股票，利润为0
        dp[0][j][1] = -prices[0]  # 第0天持有股票，需要买入
    
    for i in range(1, n):
        for j in range(k+1):
            # 第i天不持有股票：要么前一天就不持有，要么前一天持有今天卖出
            dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
            # 第i天持有股票：要么前一天就持有，要么前一天不持有今天买入
            # 买入时交易次数增加1（如果j > 0）
            if j > 0:
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])
            else:
                dp[i][j][1] = max(dp[i-1][j][1], -prices[i])
    
    return dp[n-1][k][0]


if __name__ == '__main__':
    p = [3,2,6,5,0,3]
    k = 2

    print(main(p, k))
