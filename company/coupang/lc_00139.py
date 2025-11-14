# coding=utf-8


def main(ss, words):
    dp = [False] * (len(ss) + 1)
    dp[0] = True

    for i in range(len(ss)):
        j = i
        while j>=0:
            if ss[j:i+1] in words and dp[j]:
                dp[i+1] = True
                break
            j-=1

    return dp[-1]


if __name__ == '__main__':
    # s = "leetcode"
    # wordDict = ["leet", "code"]
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    res = main(s, wordDict)
    print(res)
