# coding=utf-8

def method_1(ss, dictionary):
    """
    最直观的直线方案
    """
    dic = set(dictionary)

    strs = ss.split(' ')
    res = []
    for s in strs:
        flag = False
        for i in range(len(s)):
            c = s[:i+1]
            if c in dic:
                res.append(c)
                flag = True
                break
        if flag is False:
            res.append(s)
    
    return ' '.join(res)


def dfs(dics, i, s):
    """ 
    构建字典树
    """
    if i == len(s):
        dics[1] = None  # 加一个标识符，标识词根结束了
        return
    c = s[i]
    if c not in dics:
        dics[c] = {}
    dfs(dics[c], i+1, s)


def dfs2(i, s, dics, path):
    """ 
    从字典树中查询
    """
    if 1 in dics:  # 如果遇到结束的词根符号，则返回 True
        return True
    if i == len(s):
        return False
    if s[i] not in dics:
        return False
    path.append(s[i])
    return dfs2(i+1, s, dics[s[i]], path)

def method_2(ss, dictionary):
    dics = {}
    for s in dictionary:
        dfs(dics, 0, s)
    
    res = []
    words = ss.split()
    for word in words:
        path = []
        if dfs2(0, word, dics, path) is False:
            res.append(word)
        else:
            res.append(''.join(path))
    return ' '.join(res)


if __name__ == '__main__':
    # dictionary = ["cat","bat","rat"]
    # sentence = "the cattle was rattled by the battery"

    # dictionary = ["a","b","c"]
    # sentence = "aadsfasf absbs bbab cadsfafs"

    dictionary = ["catt","cat","bat","rat"]
    sentence = "the cattle was rattled by the battery"

    res = method_2(sentence, dictionary)
    print(res)