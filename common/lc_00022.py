# coding=utf-8
import copy
from collections import deque

def main(n):
    """ 
    计算左括号被放置的位置索引
    """
    if n == 1:
        return ['()']
    
    queue = deque()
    queue.append([0])
    
    i = 2
    while i<=n:
        ll = len(queue)
        # 在括号的基础上构建新括号
        while ll > 0:
            item = queue.popleft()
            for j in range(item[-1]+1, i*2-1):
                item_ = copy.deepcopy(item) 
                item_.append(j)
                queue.append(item_)
            ll -=1
        i+=1
    
    res = []
    while len(queue) > 0:
        res_ = [')'] * 2 * n
        item = queue.popleft()
        for i in item:
            res_[i] = '('
        res.append(''.join(res_))
    return res


if __name__ == '__main__':
    n = 2
    res = main(n)
    print(res)