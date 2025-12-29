# coding=utf-8

def main(n):
    dp = [0] * (n+1)
    dp[1] = 1
    for i in range(2, n+1):
        for j in range(1, i):
            a = max(i-j, dp[i-j])
            b = max(j, dp[j])
            dp[i] = max(dp[i], a * b)
    return dp[-1]  

if __name__ == '__main__':
    n = 9
    
    res = main(n)
    print(res)
