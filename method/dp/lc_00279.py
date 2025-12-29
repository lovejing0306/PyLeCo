# coding=utf-8

def method_1(n):
    """ 
    该实现会出现超时现象
    """
    dp = [float('inf')] * (n+1)
    
    i = 1
    while True:
        a = i * i
        if a > n:
            break
        dp[a] = 1
        i+=1
    
    for i in range(1, n+1):
        if dp[i] == 1:
            continue
    
        for j in range(1, i//2+1):
            dp[i] = min(dp[i], dp[j] + dp[i-j])
    return dp[-1]


def method_2(n):
    dp = [float('inf')] * (n+1)
    dp[0] = 0

    squares = []
    i = 1
    while i*i<=n:
        squares.append(i*i)
        i+=1
        
    for i in range(1, n+1):
        for s in squares:
            if s>i:
                break
            if dp[i-s] + 1 < dp[i]:
                dp[i] = dp[i-s] + 1
    return dp[-1]


if __name__ == '__main__':
    n = 12

    res = method_2(n)
    print(res)
