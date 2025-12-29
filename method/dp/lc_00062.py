# coding=utf-8

def main(m, n):
    dp = []
    for _ in range(m):
        dp.append([1] * n)
    
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1]


if __name__ == '__main__':
    m = 3
    n = 3
    res = main(m, n)
    print(res)