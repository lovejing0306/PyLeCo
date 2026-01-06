# coding=utf-8

def main(ss):
    dp = []
    for _ in range(len(ss)):
        dp.append([0]*len(ss))
    
    for i in range(len(ss)):
        dp[i][i] = 1
    
    for i in range(len(ss)-2+1):
        j = i + 2-1
        if ss[i] == ss[j]:
            dp[i][j] = 2
        else:
            dp[i][j] = 1
    
    for l in range(3, len(ss)+1):
        for i in range(len(ss)-l+1):
            j = i+l-1
            if ss[i] == ss[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i][j-1], dp[i+1][j])
    return dp[0][-1]


if __name__ == '__main__':
    ss = 'cbbd'
    res = main(ss)
    print(res)