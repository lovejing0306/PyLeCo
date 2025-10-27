# coding=utf-8

def main(strs, mm, nn):
    nums01 = []
    # 统计每个字符串中的字符0和字符1出现的次数
    for str_ in strs:
        count = 0
        for i in range(len(str_)):
            if str_[i] == '0':
                count += 1
        nums01.append([count, len(str_) - count])
    
    dp = []
    for _ in range(len(strs) + 1):
        dp_ = []
        for _ in range(mm + 1):
            dp_.append([0] * (nn+1))
        dp.append(dp_)

    for i in range(1, len(strs) + 1):  # 遍历每个字符串
        num0, num1 = nums01[i-1]  # 取出字符串中包含的字符0和字符1的数量
        for m in range(1, mm + 1):
            for n in range(1, nn + 1):
                if num0 > m or num1 > n:  # 如果当前字符串中的字符0和字符1数量都大于要求的数量，则取上一个状态的结果
                    dp[i][m][n] = dp[i-1][m][n]
                else:  # 考虑加入当前字符串和不加入当前的情况
                    dp[i][m][n] = max(dp[i-1][m-num0][n-num1] + 1, dp[i-1][m][n])
    return dp[len(strs)][mm][nn]


if __name__ == '__main__':
    # strs = ["10", "0001", "111001", "1", "0"]
    # m = 5
    # n = 3

    strs = ["10", "0", "1"]
    m = 1
    n = 1
    res = main(strs, m, n)
    print(res)
