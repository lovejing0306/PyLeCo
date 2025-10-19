# coding=utf-8

def main(piles):
    n = len(piles)
    # dp[i][j] 表示在 piles[i:j+1] 区间内,先手比后手多拿的最大分数
    dp = [[0] * n for _ in range(n)]
    # 只有一堆石子时,先手直接拿走
    for i in range(n):   # 剩余 一堆 石头
        dp[i][i] = piles[i]
    
    for length in range(2, n+1):  # 剩余 石头的堆数
        for i in range(n-length+1):  # 左区间值
            j = i + length -1  # 右区间值
            # 先手选择左边或右边
            # 选左边: piles[i] - dp[i+1][j] (因为对手在剩余区间先手)
            dp[i][j] = max(piles[i] -dp[i+1][j], piles[j] - dp[i][j-1])
    return dp[0][n-1] > 0


if __name__ == '__main__':
    a=[5,3,4,5]
    print(main(a))