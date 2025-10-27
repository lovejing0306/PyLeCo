# coding=utf-8

def main(n, c, weights, values, nums):
    """
    如果从解决问题的角度看，可以通过展平的方式把其他背包问题都转成 0-1 背包问题
    """
    weights_ = []
    values_ = []

    for i in range(n):
        weights_.extend([weights[i]] * nums[i])
        values_.extend([values[i]] * nums[i])

    dp = []
    for _ in range(len(weights_) + 1):
        dp.append([0] * (c+1))
    
    for i in range(1, len(dp)):  # 从索引 1 开始，先遍历物品
        for j in range(1, c+1):  # 从索引 1 开始，再遍历物品
            if weights_[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j-weights_[i-1]] + values_[i-1], dp[i-1][j])
    
    return dp[len(weights_)][c]


if __name__ == '__main__':
    n=4
    c=5
    weights = [1,2,3,4]
    values = [2,4,4,5]
    nums = [3,1,3,2]

    res = main(n, c, weights, values, nums)
    print(res)