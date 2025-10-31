# coding=utf-8

def main(w1, w2):
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
    res = main(w1, w2)
    print(res)
