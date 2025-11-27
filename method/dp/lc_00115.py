# coding=utf-8
def method_2(s, t):
    dp = []
    for i in range(len(t)+1):
        if i == 0:  # 索引为 0 的位置表示 空字符串
            dp.append([1] * (len(s) + 1))   # 空字符串对应行为全 1
        else:
            dp.append([0] * (len(s) + 1))

    for i in range(1, len(t) + 1):
        for j in range(i, len(s) + 1):
            if t[i-1] == s[j-1]:
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
            else:
                dp[i][j] = dp[i][j-1]
    return dp[-1][-1]


def main(s, t):
    if len(s) == 0 or len(t) == 0:
        return 0
    
    dp = []
    for _ in range(len(t)):
        dp.append([0] * len(s))
    sum = 0
    for i in range(len(s)):
        if t[0] == s[i]:
            sum+=1
        dp[0][i] = sum  # 这里的初始化很关键
    
    for i in range(1, len(t)):
        for j in range(i, len(s)):
            if t[i] == s[j]:
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
            else:
                dp[i][j] = dp[i][j-1]
    return dp[len(t)-1][len(s)-1]


if __name__ == '__main__':
    s = "rabbbit"
    t = "rabbit"
    # s = "babgbag"
    # t = "bag"
    res = method_2(s, t)
    print(res)