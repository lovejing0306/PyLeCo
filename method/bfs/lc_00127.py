# coding=utf-8

def is_valid(str1, str2):
    count = 0
    for i in range(len(str1)):
        c1 = str1[i]
        c2 = str2[i]
        if c1 != c2:
            count+=1
        if count > 1:
            return False
    return True if count == 1 else False


def method_1(beginWord, endWord, wordList):
    """ 
    没有超时，勉强通过
    """
    wordSet = set(wordList)
    if endWord not in wordSet:
        return 0

    mapping = {}
    for i in range(len(wordList)):
        w1 = wordList[i]
        for j in range(i+1, len(wordList)):
            w2 = wordList[j]
            if is_valid(w1, w2):
                if w1 in mapping:
                    mapping[w1].append(w2)
                else:
                    mapping[w1] = [w2]
                if w2 in mapping:
                    mapping[w2].append(w1)
                else:
                    mapping[w2] = [w1]

    for i in range(len(wordList)):
        w2 = wordList[i]
        if is_valid(beginWord, w2):
            if beginWord in mapping:
                mapping[beginWord].append(w2)
            else:
                mapping[beginWord] = [w2]
    
    queue = [beginWord]
    visited = {beginWord}
    count = 0
    flag = False

    while len(queue) > 0:
        new_queue = []
        for ww in queue:
            if ww == endWord:
                flag = True
                break
            for w in mapping.get(ww, []):
                if w not in visited:
                    new_queue.append(w)
                    visited.add(w)
        count +=1
        if flag is True:
            break
        queue = new_queue
    return count if flag else 0


def method_2(beginWord, endWord, wordList):
    """ 
    执行效率改善的方案2
    """
    wordSet = set(wordList)
    if endWord not in wordSet:  # 如果结束单词不在单词表中，则直接返回 0
        return 0

    chars = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g',
        'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u',
        'v', 'w', 'x', 'y', 'z'
    ]

    # 127
    visited = {beginWord}  # 将起始单词添加到已经访问过的集合中
    queue = [beginWord]  # 将起始单词添加到起始队列中
    count = 1
    flag = False

    while len(queue) > 0:
        new_queue = []  # 创建新的队列
        for w in queue:  # 访问队列中的每个元素
            if w == endWord:  # 如果访问到的当前单词是 结束单词，则结束循环
                flag = True
                break
            for c in chars:  # 访问每个字符，使用字符构建新的单词
                for i in range(len(w)):
                    if i == 0:
                        c_ = c + w[i+1:]
                    elif i == len(w)-1:
                        c_ = w[:-1] + c
                    else:
                        c_ = w[:i] + c + w[i+1:]
                    # 如果构建的单词在单词列表中，同时没有在访问集合中出现，则把构建单词添加到新的队列，同时添加到访问的集合中
                    if c_ in wordSet and c_ not in visited:
                        new_queue.append(c_)
                        visited.add(c_)
        if flag:
            break
        count += 1
        queue = new_queue  # 替换队列
    return count if flag else 0  # 只有在找到的情况下，才能输出统计只 count


if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    res = method_2(beginWord, endWord, wordList)
    print(res)