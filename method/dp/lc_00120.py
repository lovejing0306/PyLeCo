# coding=utf-8

def main(triangle):
    m = len(triangle)
    n = len(triangle[-1])
    
    dp = []
    for _ in range(m):
        dp.append([float('inf')] * n)
    
    dp[0][0] = triangle[0][0]
    for i in range(1, m):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][j] = triangle[i][j] + dp[i-1][j]
            else:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
    return min(dp[-1])


if __name__ == '__main__':
    triangle = [[-10]]
    res = main(triangle)
    print(res)