# coding=utf-8
import sys

def main(words):
    counter = []

    for word in words:
        chars = [0] * 26
        for c in word:
            chars[ord(c)-ord('a')] += 1
        counter.append(chars)  # 记录每个单词对应的 字符映射
    
    res = []
    for i in range(26):
        min_v = sys.maxsize
        for j in range(len(words)):
            min_v = min(min_v, counter[j][i])
        
        res.extend([chr(ord('a') + i)] * min_v)
    return res
    

if __name__ == '__main__':
    words = ["cool","lock","cook"]
    res = main(words)
    print(res)
