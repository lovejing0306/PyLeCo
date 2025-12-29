# coding=utf-8

def main(text1, text2):
    m = len(text1)
    n = len(text2)

    dp = []
    for _ in range(m):
        dp.append([0] * n)

    for i in range(0, m):
        if text1[i] == text2[0]:
            for k in range(i, m):
                dp[k][0] = 1  # 将后面全部赋值为 1
            break
    
    for j in range(0, n):
        if text1[0] == text2[j]:
            for k in range(j, n):
                dp[0][k] = 1  # 将后面全部赋值为 1
            break
    
    for i in range(1, m):
        for j in range(1, n):
            if text1[i] == text2[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]


if __name__ == '__main__':
    t1 = 'abc'
    t2 = 'def'

    res = main(t1, t2)
    print(res)
