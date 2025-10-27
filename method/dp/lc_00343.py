# coding=utf-8

def main(n):
    dp = [1] * (n+1)

    for i in range(2, n+1):
        j = i-1
        max_value = -1
        while j >=1:
            # max(dp[j], j) 这一步很关键，从当前索引值和它对应的dp值中取最大
            max_value = max(max(dp[j], j)* (i-j), max_value)
            j-=1
        dp[i] = max_value
    return dp[n]


if __name__ == '__main__':
    res = main(10)
    print(res)
