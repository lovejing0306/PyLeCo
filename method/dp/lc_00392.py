# coding=utf-8

from sre_compile import JUMP


def main(s, t):
    if len(s)==0 or len(t) ==0:
        return False
    
    dp = []
    for _ in range(len(s)):
        dp.append([False] * len(t))
    
    for i in range(len(t)):
        if s[0] == t[i]:
            while i < len(t):
                dp[0][i] = True
                i+=1
            break
    
    for i in range(1, len(s)):
        for j in range(1, len(t)):
            if s[i] == t[j]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = dp[i][j-1]   # 这一步相当于是删除
    return dp[len(s)-1][len(t)-1]


if __name__ == '__main__':
    # s = "abc"
    # t = "ahbgdc"
    s = "axc"
    t = "ahbgdc"
    res = main(s, t)
    print(res)