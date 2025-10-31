# coding=utf-8

def main(s1, s2):
    if len(s1) == 0 or len(s2)==0:
        return 0

    dp = []
    for _ in range(len(s1)):
        dp.append([0] * len(s2))
    
    for i in range(0, len(s1)):
        if s1[i] == s2[0]:
            while i < len(s1):
                dp[i][0] = 1
                i+=1
            break
    
    for i in range(0, len(s2)):
        if s1[0] == s2[i]:
            while i < len(s2):
                dp[0][i] = 1
                i+=1
            break
    
    for i in range(1, len(s1)):
        for j in range(1, len(s2)):
            if s1[i] == s2[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(max(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1])
    
    return dp[len(s1)-1][len(s2)-1]


if __name__ == '__main__':
    text1 = "abc"
    text2 = "ace" 
    res = main(text1, text2)
    print(res)
