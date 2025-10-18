# coding=utf-8

import queue

def bfs(begin_word, end_word, word_list):
    word_set = set(word_list)

    if end_word not in word_set:
        return 0

    qq = queue.Queue()
    qq.put(begin_word)  # 将起始单词放入到队列中

    visited = set()  # 记录单词是否被访问过
    visited.add(begin_word)  
    
    count = 0
    while qq.qsize() > 0:

        for _ in range(qq.qsize()):  # 访问每一层单词
            word = qq.get()
            if word == end_word:  # 如果找到了结束单词，直接返回
                return count + 1
            
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':  # 访问 26 个英文字母
                    if c == word[i]:  # 如果和当前替换的字母相同，则跳过
                        continue
                    replace_word = word[:i] + c + word[i+1:]
                    
                    if replace_word in visited:  # 如果替换后的单词已经被访问过，则跳过
                        continue
                    if replace_word not in word_set:  # 如果替换后的单词不在集合中，则跳过
                        continue
                    qq.put(replace_word)  # 添加新的同一层单词
                    visited.add(replace_word)  # 将新的单词添加到被访问集合中
        count += 1
    return 0


if __name__ == '__main__':
    begin_word = "hit"
    end_word = "cog"
    word_list = ["hot","dot","dog","lot","log","cog"]

    count = bfs(begin_word, end_word, word_list)
    print(count)
