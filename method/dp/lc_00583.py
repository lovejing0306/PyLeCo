# coding=utf-8

def method_2(w1, w2):
    if len(w1) == 0:
        return len(w2)
    if len(w2) == 0:
        return len(w1)
    
    dp = []
    for _ in range(len(w1)):
        dp.append([0] * len(w2))
    
    for i in range(len(w1)):
        if w1[i] == w2[0]:
            dp[i][0] = i
        else:
            if i == 0:
                dp[i][0] = 2  # 如果索引为 0 ，则两个都需要删除
            else:
                dp[i][0] = dp[i-1][0] + 1  # 这里相当于删除了第 i 个字符，同时从 dp[i-1][0] 取最小
    
    for j in range(len(w2)):
        if w1[0] == w2[j]:
            dp[0][j] = j
        else:
            if j == 0:
                dp[0][j] = 2
            else:
                dp[0][j] = dp[0][j-1]+1
    
    for i in range(1, len(w1)):
        for j in range(1, len(w2)):
            if w1[i] == w2[j]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1]+2, min(dp[i-1][j], dp[i][j-1])+1)
    return dp[-1][-1]
            

def method_1(w1, w2):
    if len(w1) == 0:
        return len(w2)
    
    if len(w2) == 0:
        return len(w1)
    
    dp = []
    for _ in range(len(w1) + 1):
        dp.append([0] * (len(w2) + 1))
    
    for i in range(1, len(w1) + 1):
        dp[i][0] = i
    
    for i in range(1, len(w2) + 1):
        dp[0][i] = i

    for i in range(1, len(w1) + 1):
        for j in range(1, len(w2) + 1):
            if w1[i-1] == w2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1] + 2, min(dp[i][j-1], dp[i-1][j]) + 1)
    return dp[len(w1)][len(w2)]


if __name__ == '__main__':
    w1 = 'sea'
    w2 = 'eat'
    res = method_1(w1, w2)
    print(res)
