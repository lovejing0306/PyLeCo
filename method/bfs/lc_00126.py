# coding=utf-8

def is_next(s1, s2):
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:  # 判断每个位置上的字符是否相同
            count += 1
    return True if count == 1 else False


def method_1(beginWord, endWord, wordList):
    """
    超出了内存
    """
    wordSet = set(wordList)
    if endWord not in wordSet:
        return []
    # 查找每个单词对应的相邻单词
    mapping = {word : [] for word in wordList}
    for i in range(len(wordList)):
        for j in range(i+1, len(wordList)):
            if is_next(wordList[i], wordList[j]):
                mapping[wordList[i]].append(wordList[j])
                mapping[wordList[j]].append(wordList[i])
    
    queue = []  # 存放的是路径
    # 查找从起始单词到达的单词
    for i in range(len(wordList)):
        if is_next(beginWord, wordList[i]):
            queue.append([beginWord, wordList[i]])
    
    flag = False
    res = []  # 记录符合条件的最短路径
    while len(queue) > 0:
        new_queue = []
        for path in queue:
            word = path[-1]
            if word == endWord:
                res.append(path[:])
                flag = True
            path_set = set(path)
            for next_w in mapping[word]:
                if next_w in path_set:
                    continue
                path_ = path[:]
                path_.append(next_w)
                new_queue.append(path_)
    
        queue = new_queue
        if flag:
            break
    return res


def method_2(beginWord, endWord, wordList):
    wordSet = set(wordList)
    if endWord not in wordSet:
        return []
    parents = {}
    found = False
    level = {beginWord}
    visited = {beginWord}
    while level and not found:
        next_level = set()
        local_visited = set()
        for word in level:
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c == word[i]:
                        continue
                    nxt = word[:i] + c + word[i+1:]
                    if nxt not in wordSet:
                        continue
                    if nxt not in visited:
                        if nxt not in parents:
                            parents[nxt] = set()
                        parents[nxt].add(word)
                        if nxt not in local_visited:
                            next_level.add(nxt)
                            local_visited.add(nxt)
        if endWord in next_level:
            found = True
        visited |= local_visited
        level = next_level
    if not found:
        return []
    res = []
    path = [endWord]
    def dfs(word):
        if word == beginWord:
            res.append(path[::-1])
            return
        for p in parents.get(word, []):
            path.append(p)
            dfs(p)
            path.pop()
    dfs(endWord)
    return res

if __name__ == '__main__':
    s1 = 'hit'
    s2 = 'cog'
    # res = is_next(s1, s2)
    # print(res)
    # words = ["hot","dot","dog","lot","log","cog"]
    words = ["hot","dot","dog","lot","log"]
    res = method_1(s1, s2, words)
    print(res)