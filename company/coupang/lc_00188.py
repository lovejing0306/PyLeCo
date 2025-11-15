# coding=utf-8

def main(prices, k):
    dp = []
    for _ in range(len(prices)):
        tt = []
        for _ in range(k+1):
            tt.append([0, 0])
        dp.append(tt)
    
    for k_ in range(1, k+1):
        dp[0][k_][0] = -prices[0]

    for i in range(1, len(prices)):
        for k_ in range(1, k+1):
            # dp[i-1][k_][0] 的前一个状态是 dp[i-1][k_-1][1]
            dp[i][k_][0] = max(dp[i-1][k_][0], dp[i-1][k_-1][1] - prices[i])  # 这里是 k_-1 ！！！
            dp[i][k_][1] = max(dp[i-1][k_][1], dp[i-1][k_][0] + prices[i])
    return dp[-1][k][1]


if __name__ == '__main__':
    k = 2
    prices = [2,4,1]

    res = main(prices, k=k)
    print(res)