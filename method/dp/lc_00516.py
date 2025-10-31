# coding=utf-8

def main(ss):
    if len(ss) == 0:
        return 0
    if len(ss) == 1:
        return 1
    
    if len(ss) == 2:
        return 2 if ss[0] == ss[1] else 1

    dp = []
    for _ in range(len(ss)):
        dp.append([0] * len(ss))
    
    max_value = 1
    for i in range(len(ss)):
        dp[i][i] = 1
    
    for i in range(len(ss)-1):
        if ss[i] == ss[i+1]:
            dp[i][i+1] = 2
        else:
            dp[i][i+1] = 1
        max_value = max(max_value, dp[i][i+1])

    for k in range(2, len(ss)):
        for i in range(len(ss)-k):
            j = i+k
            if ss[i] == ss[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j-1], max(dp[i][j-1], dp[i+1][j]))  # 从三种情况中取最大
            max_value = max(max_value, dp[i][j])
    return max_value


if __name__ == '__main__':
    ss = 'cbbd'
    res = main(ss)
    print(res)
