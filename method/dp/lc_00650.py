# coding=utf-8

def main(n):
    dp = list(range(n+1))   # 初始化 dp 数组
    dp[1] = 0  # 边界条件处理，n=1 时，取值为 0
    # 从下标 1 开始
    for i in range(1, n+1):
        j= i-1   # 从当前索引 i 往前遍历
        while j>=1:
            if i % j == 0:  # 如果 i 可以整除 j，则长度为 i 的 A 可以通过 j 构造
                dp[i] = min(dp[i], dp[j] + i//j)  # 具体的状态转移方程
            j-=1
    return dp[-1]

if __name__ == '__main__':
    res = main(1)
    print(res)