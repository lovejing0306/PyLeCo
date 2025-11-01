# coding=utf-8

def method_1(ss):
    """
    该方案会超时
    """
    if len(ss) == 0 or len(ss) == 1:
        return 0
    
    if len(ss) == 2:
        return 0 if ss[0] == ss[1] else 1

    dp_flag = []
    for _ in range(len(ss)):
        dp_flag.append([0]*len(ss))
    
    for i in range(len(ss)):
        dp_flag[i][i] = 1

    for i in range(len(ss)-1):
        if ss[i]==ss[i+1]:
            dp_flag[i][i+1] = 1
    
    for k in range(2, len(ss)):
        for i in range(len(ss)-k):
            j = i + k
            if ss[i] == ss[j] and dp_flag[i+1][j-1] == 1:
                dp_flag[i][j] = 1

    dp = []
    for _ in range(len(ss)):
        dp.append([float('inf')] * len(ss))

    for i in range(len(ss)):
        dp[i][i] = 0
    for i in range(len(ss)-1):
        if ss[i]==ss[i+1]:
            dp[i][i+1] = 0
        else:
            dp[i][i+1] = 1
    
    for k in range(2, len(ss)):
        for i in range(len(ss)-k):
            j = i + k
            if ss[i] == ss[j] and dp_flag[i+1][j-1] == 1:
                dp[i][j] = 0
            else:
                for p in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][p] + dp[p+1][j])
                dp[i][j] = dp[i][j] + 1

    for i in range(len(dp)):
        print(dp[i])
    return dp[0][len(ss)-1]


def method_2(ss):
    """
    该方案会超时
    """
    if len(ss) == 0 or len(ss) == 1:
        return 0
    
    if len(ss) == 2:
        return 0 if ss[0] == ss[1] else 1

    dp_flag = []
    for _ in range(len(ss)):
        dp_flag.append([0]*len(ss))
    
    for i in range(len(ss)):
        dp_flag[i][i] = 1

    for i in range(len(ss)-1):
        if ss[i]==ss[i+1]:
            dp_flag[i][i+1] = 1
    
    for k in range(2, len(ss)):
        for i in range(len(ss)-k):
            j = i + k
            if ss[i] == ss[j] and dp_flag[i+1][j-1] == 1:
                dp_flag[i][j] = 1

    dp = [float('inf')] * len(ss)
    dp[0] = 0
    
    for i in range(1, len(ss)):
        j=i
        while j>=0:
            if dp_flag[j][i] == 1:  # j～i 不是回文串的情况那？
                if j == 0:
                    dp[i] = 0
                else:
                    dp[i] = min(dp[j-1] + 1, dp[i])
            j-=1

    return dp[len(ss)-1]
 

if __name__ == '__main__':
    ss = 'aab'
    # res = method_1(ss)
    res = method_2(ss)
    print(res)
