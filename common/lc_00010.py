# coding=utf-8

def main(s, p):
    dp = []
    for _ in range(len(s)+1):
        dp.append([False] * (len(p)  +1))

    dp[0][0] = True  # 空字符串是匹配的
    
    for j in range(2, len(p) +1):
        if p[j-1] == '*':  # 如果是 * 的话，可以默认匹配 0 个字符，相当于把前一个字符给删除掉
            dp[0][j] = dp[0][j-2]
    
    for i in range(1, len(s)  +1):
        for j in range(1, len(p) + 1):
            if p[j-1] != '*':
                if p[j-1] == s[i-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
            else:  # 如果是 *
                # 匹配 0 次
                dp[i][j] = dp[i][j-2]
                # 匹配 1 次，及以上
                if p[j-2] == s[i-1] or p[j-2] == '.':
                    dp[i][j] = dp[i][j] or dp[i-1][j]
    return dp[-1][-1]


if __name__ == '__main__':
    s = "aa"
    p = "a*"

    res = main(s, p)
    print(res)
