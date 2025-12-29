# coding=utf-8

class NumMatrix:

    def __init__(self, matrix):
        self.dp = []
        self.m = len(matrix)
        self.n = len(matrix[0])

        for _ in range(self.m):
            self.dp.append([0] * self.n)
        
        sum_ = 0
        for i in range(self.m):
            sum_ += matrix[i][0]
            self.dp[i][0] = sum_
        sum_ = 0
        for j in range(self.n):
            sum_ += matrix[0][j]
            self.dp[0][j] = sum_
        
        for i in range(1, self.m):
            for j in range(1, self.n):
                self.dp[i][j] = self.dp[i-1][j] + self.dp[i][j-1] - self.dp[i-1][j-1] + matrix[i][j]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        x1 = row2
        y1 = col1-1
        x2 = row1-1
        y2 = col2
        x3 = row1-1
        y3 = col1-1
        res = self.dp[row2][col2]

        if 0<=x1 < self.m and 0 <=y1 < self.n:
            res -= self.dp[x1][y1]
        if 0<=x2 < self.m and 0 <= y2 < self.n:
            res -= self.dp[x2][y2]
        if 0<=x3 < self.m and 0<=y3 < self.n:
            res += self.dp[x3][y3]
        return res

if __name__ == '__main__':
    matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
    aa = NumMatrix(matrix)
    res = aa.sumRegion(1, 1, 2, 2)
    print(res)