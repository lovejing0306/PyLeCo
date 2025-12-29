# coding=utf-8

def main(ss, words):
    word_dict = {}  # 记录不同的长度的单词
    # 统计不同长度的单词
    for word in words:
        l = len(word)
        if l in word_dict:
            word_dict[l].add(word)
        else:
            word_dict[l] = {word}
    
    dp = [[] for _ in range(len(ss) + 1)]  # 这里需要创建不同地址的 list
    
    for i in range(1, len(dp)):   # 从单词长度为 1 的开始遍历
        for key in word_dict.keys():  # 访问不同长度的单词
            j = i - key  # 计算单词的起始索引
            if j < 0:
                continue
            sub_word = ss[j:i]   # 获取子单词
            if sub_word in word_dict[key]:   # 如果子单词在该长度的单词集合中
                if j == 0:   # 如果 j 为0 ！！！
                    dp[i].append(sub_word)
                else:
                    for k in range(len(dp[j])):
                        s = dp[j][k]
                        dp[i].append(s + ' ' + sub_word)  # 构建新的字符串
    return dp[-1]


if __name__ == '__main__':
    s = 'pineapplepenapple'
    words = ["apple","pen","applepen","pine","pineapple"]
    res = main(s, words)
    print(res)