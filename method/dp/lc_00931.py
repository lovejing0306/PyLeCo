# coding=utf-8

def main(matrix):
    m = len(matrix)
    n = len(matrix[0])

    dp = []
    for _ in range(m):
        dp.append([float('inf')] * n)
    
    for j in range(n):
        dp[0][j] = matrix[0][j]

    dirs = [(-1, -1), (-1, 0), (-1, 1)]

    for i in range(1, m):
        for j in range(0, n):
            for item in dirs:
                x = i + item[0]
                y = j + item[1]
                if 0<=x < m and 0<=y < n:
                    dp[i][j] = min(dp[i][j], dp[x][y]+matrix[i][j])
    return min(dp[-1])


if __name__ == '__main__':
    matrix = [[-19,57],[-40,-5]]
    res = main(matrix)
    print(res)