# coding=utf-8

def is_single(ss, i):
    if '1' <= ss[i] <= '9':  # 字符 1～9 是合法字符
        return True
    else:
        return False


def is_double(ss, i):
    # 前一个字符必须是 1 或者 2，且两个字符组成的数字必须在 10 ～ 26 之间
    if (ss[i-1] == '1' or ss[i-1] == '2') and '10' <= ss[i-1:i+1] <='26':
        return True
    else:
        return False


def main(ss):
    if ss[0] == '0':  # 如果第一个字符是 0 ，直接返回
        return 0

    dp = [0] * (len(ss) + 1)
    dp[0] = 1
    dp[1] = 1  # 第一个合法字符默认为 1

    for i in range(2, len(ss)+1):
        c1 = dp[i-1] if is_single(ss, i-1) else 0  # 当前字符组成的合法个数
        c2 = dp[i-2] if is_double(ss, i-1) else 0  # 当前字符和前一个字符组成的合法个数
        dp[i] = c1 + c2
    return dp[-1]


if __name__ == '__main__':
    s = "12"
    res = main(s)
    print(res)