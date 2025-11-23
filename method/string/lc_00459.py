# coding=utf-8

def main(s):
    prefix = [0] * len(s)

    j = 0
    for i in range(1, len(s)):
        while j>0 and s[i] !=s[j]:
            j = prefix[j-1]
        if s[i]==s[j]:
            j+=1
        prefix[i] = j
    # prefix[-1] 记录了匹配的最长字符串长度
    return True if prefix[-1] > 0 and  len(s) % (len(s)-prefix[-1]) == 0 else False


if __name__ == '__main__':
    s = 'aba'
    res = main(s)
    print(res)
