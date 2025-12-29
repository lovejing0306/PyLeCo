# coding=utf-8

def main(grid):
    if grid[0][0] == 1:
        return 0

    m = len(grid)
    n = len(grid[0])

    dp = []
    for _ in range(m):
        dp.append([0] * n)

    for i in range(m):
        if grid[i][0] == 0:
            dp[i][0] = 1
        else:
            break
    for j in range(n):
        if grid[0][j] == 0:
            dp[0][j] = 1
        else:
            break
    
    for i in range(1, m):
        for j in range(1, n):
            if grid[i][j] == 1:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[-1][-1]

if __name__ == '__main__':
    grid = [[0,1],[0,0]]
    res = main(grid)
    print(res)