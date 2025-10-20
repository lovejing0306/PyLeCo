# coding=utf-8

def main(ss, word_dict):
    word_dict = set(word_dict)
    # 状态：字符串中的前 i 个字符是否可以由 word_dict 中的单词组合成
    dp = [False] * (len(ss) +1)
    
    dp[0] = True  # 没有字符串时，默认为 True

    for i in range(1, len(dp)):  # 遍历从字符串长度从 1 到 n 的情况
        j = i-1
        while j>=0:
            sub_ss = ss[j:i]  # 截取子字符串
            dp[i] = dp[j] and sub_ss in word_dict
            if dp[i]:
                break
            j -=1
    return dp[len(ss)]


if __name__ == '__main__':
    ss = 'leetcode'
    word_dict = ["leet", "code"]

    print(main(ss, word_dict))
    