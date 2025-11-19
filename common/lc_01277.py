# coding=utf-8

def main(matrix):
    """
    重点要放在 正方形数量上 
    """
    m = len(matrix)
    n = len(matrix[0])

    dp = []
    for _ in range(m):
        dp.append([0] * n)
    
    res = 0
    for i in range(m):
        if matrix[i][0] == 1:
            dp[i][0] = 1
            res += 1
    
    for j in range(1, n):
        if matrix[0][j] == 1:
            dp[0][j] = 1
            res += 1
    
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 1:
                matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
                res += matrix[i][j]
    return res
