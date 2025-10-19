# coding=utf-8

def main(text1, text2):
    m = len(text1)
    n = len(text2)

    dp = [[0]*n for _ in range(m)]

    for i in range(m):
        if text1[i] == text2[0]:
            while i < m:
                dp[i][0] = 1
                i+=1
            break

    for i in range(n):
        if text1[0] == text2[i]:
            while i<n:
                dp[0][i] = 1
                i+=1
            break
    
    for i in range(1, m):
        for j in range(1, n):
            if text1[i] == text2[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])

    return dp[m-1][n-1]


if __name__ == '__main__':
    s1 = 'ace'
    s2 = 'def'

    res = main(s1, s2)
    print(res)