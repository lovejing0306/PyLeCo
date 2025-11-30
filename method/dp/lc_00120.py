# coding=utf-8
import sys

def main(triangle):
    m = len(triangle)
    n = len(triangle[-1])

    dp = []
    for _ in range(m):
        dp.append([sys.maxsize] * n)

    tt = 0
    for i in range(m):
        tt += (triangle[i][0])
        dp[i][0] = tt
    
    for i in range(1, m):
        for j in range(1, len(triangle[i])):
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
    return min(dp[-1])


if __name__ == '__main__':
    # nums = [[2],[3,4],[6,5,7],[4,1,8,3]]
    nums = [[-10]]
    res = main(nums)
    print(res)