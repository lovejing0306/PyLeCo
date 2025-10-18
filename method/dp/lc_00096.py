# coding=utf-8

def main(n):
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n+1):  # 这里遍历的是节点数量
        sum = 0
        for j in range(1, i+1):  # 这里遍历的是以数字 i 做 根节点是构成的子树数量
            sum = sum + dp[j-1] * dp[i-j]
        dp[i] = sum
    return dp[n]

if __name__ == '__main__':
    print(main(4))
