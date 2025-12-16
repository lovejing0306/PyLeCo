# coding=utf-8

""" 
给你两个单词 word1 和 word2，请返回将 word1 转换成 word2 所使用的最少操作数

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符

示例 1：

输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例 2：

输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')

提示：
0 <= word1.length, word2.length <= 500
word1 和 word2 由小写英文字母组成

class Solution {
public:
    int minDistance(string word1, string word2) {

    }
};

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

"""


def main(w1, w2):
    if len(w1) == 0:
        return len(w2)
    if len(w2) == 0:
        return len(w1)

    dp = []
    for _ in range(len(w1) + 1):
        dp.append([0] * (len(w2) + 1))
    
    for i in range(1, len(w1) + 1):
        dp[i][0] = i
    for i in range(1, len(w2) + 1):
        dp[0][i] = i
    
    for i in range(1, len(w1)+1):
        for j in range(1, len(w2)+1):
            if w1[i-1] == w2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1], min(dp[i][j-1], dp[i-1][j])) + 1
    return dp[len(w1)][len(w2)]

if __name__ == '__main__':
    # w1 = 'horse'
    # w2 = 'ros'
    w1 = "intention"
    w2 = "execution"
    res = main(w1, w2)
    print(res)

