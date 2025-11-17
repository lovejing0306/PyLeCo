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
            dp[i][0] = i  # 如果 w1 的第 i 个字符等于 w2 的第 0 个字符，则需要删除 i+1-1 个字符 
        else:
            if i==0:
                dp[i][0] = 1  # 如果 i 是第 0 字符，则直接赋值为 1
            else:
                dp[i][0] = dp[i-1][0] + 1  # 如果 i 不是第 0 个字符，则去前一个结果 + 1
    
    for j in range(len(w2)):
        if w1[0] == w2[j]:
            dp[0][j] = j
        else:
            if j == 0:
                dp[0][j] = 1
            else:
                dp[0][j] = dp[0][j-1] + 1
    
    for i in range(1, len(w1)):
        for j in range(1, len(w2)):
            if w1[i]==w2[j]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1])) + 1
    return dp[-1][-1]


def main(w1, w2):
    if len(w1) == 0:
        return len(w2)

    if len(w2) == 0:
        return len(w1)

    dp = []
    for _ in range(len(w1)+1):
        dp.append([0] * (len(w2)+1))
    
    for i in range(1, len(w1) + 1):
        dp[i][0] = i
    
    for i in range(1, len(w2) + 1):
        dp[0][i] = i
    
    for i in range(1, len(w1) + 1):
        for j in range(1, len(w2) + 1):
            if w1[i-1] == w2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1], min(dp[i][j-1], dp[i-1][j])) + 1
    return dp[len(w1)][len(w2)]


if __name__ == '__main__':
    w1 = 'intention'
    w2 = 'execution'

    res = main(w1, w2)
    print(res)