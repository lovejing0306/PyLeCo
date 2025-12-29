# coding=utf-8

def main(ss, tt):
    m = len(tt)
    n = len(ss)

    dp = []
    for _ in range(m):
        dp.append([0] * n)
    
    sum_ = 0
    for j in range(n):
        if tt[0] == ss[j]:
            sum_ += 1
        dp[0][j] = sum_
    
    for i in range(1, m):
        for j in range(i, n):
            if tt[i] == ss[j]:
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
            else:
                dp[i][j] = dp[i][j-1]
    return dp[-1][-1]


if __name__ == '__main__':
    s = 'rabbbit'
    t = 'rabbit'
    # s = 'babgbag'
    # t = 'bag'
    res = main(s, t)
    print(res)
