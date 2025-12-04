# coding=utf-8

def main(prices):
    """ 
    ### 状态
    dp[0][0] = 0;   // 0: 表示不持有
    dp[0][1] = -prices[0];  // 1: 表示持有
    dp[0][2] = 0;  // 2: 表示冷冻期

    ### 转移方程
    - dp[i][0] = max(dp[i - 1][0], max(dp[i - 1][1] + prices[i], dp[i-1][2])); // 0 不持有 保持昨天不持有金额，保持昨天持有今天卖出金额，保持昨天冷冻的金额
    - dp[i][1] = max(dp[i - 1][1], dp[i - 1][2] - prices[i]);  // 1 持有   昨天冷冻金额-买入，保持昨天持有
    - dp[i][2] = max(dp[i - 1][2], dp[i - 1][0]);  // 2 冷冻   保持昨天冷冻，保持昨天不持有
    """

    dp = []
    for i in range(len(prices)):
        dp.append([0] * 3)
    
    dp[0][0] = 0  # 0: 表示不持有
    dp[0][1] = -prices[0]  # 1: 表示持有
    dp[0][2] = 0  # 2: 表示冷冻期

    for i in range(1, len(prices)):
        # 0 不持有 保持昨天不持有金额，保持昨天持有今天卖出金额，保持昨天冷冻的金额
        dp[i][0] = max(dp[i-1][0], dp[i-1][2], dp[i-1][1] + prices[i])
        # 1 持有   昨天冷冻金额-买入，保持昨天持有
        dp[i][1] = max(dp[i-1][1], dp[i-1][2]-prices[i])  # 如果今天持有，则前一天必须为 冻结 状态
        # 2 冷冻   保持昨天冷冻，保持昨天不持有
        dp[i][2] = max(dp[i-1][2], dp[i-1][0])
    return max(dp[-1][0], dp[-1][2])

if __name__ == '__main__':
    nums = [1,2,3,0,2]
    res = main(nums)
    print(res)