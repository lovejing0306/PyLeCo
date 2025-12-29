# coding=utf-8

def main(n):
    """ 
    0 --> 0
    1 --> 1
    2 --> 10
    3 --> 11
    4 --> 100
    5 --> 101
    6 --> 110
    7 --> 111
    8 --> 1000
    9 --> 1001
    10 -> 1010
    11 -> 1011
    """
    dp = [0] * (n+1)
    if n == 0:
        return dp
    dp[1] = 1
    if n == 1:
        return dp
    
    for i in range(2, n+1):
        a = i // 2
        b = i % 2

        dp[i] = dp[a] + b  # 当前数字的二进制中 1 的个数=当前数字除以 2 的商中 1 的个数 + 当前数字除以 2 的余数
    return dp

if __name__ == '__main__':
    n = 101
    res = main(n)
    print(res)
