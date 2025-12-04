# coding=utf-8
from collections import deque

def main(ss):
    """ 
    思路：寻找连续的 0 序列和 1 序列
    """
    queue = deque()

    num_zero = 0  # 记录队列中 0 出现的次数
    num_ones = 0  # 记录队列中 1 出现的次数
    res = 0   # 记录满足条件的子序列

    i = 0
    while i<len(ss):
        while i<len(ss) and ss[i] == '0':  # 如果当前字符是 0 
            queue.append(0)  # 将 0 加入到队列
            num_zero +=1   # 将记录 0 的数 +1
            i+=1  # 更新索引
        if num_zero > 0 and num_ones > 0:  # 如果 0 和 1 数量都大于 0 
            res += min(num_zero, num_ones)  # 可以构成子序列的数量为 0 和 1 数量中的最小值
            if queue[0] == 0:  # 如果队列的首元素为 0
                while num_zero > 0:  # 弹出当前队列中所有的 0
                    queue.popleft()
                    num_zero -=1  # 记录的 0 数量自减
            else:
                while num_ones > 0:  # 弹出当前队列中所有的 1
                    queue.popleft()
                    num_ones -=1  # 记录的 1 数量自减
        
        while i<len(ss) and ss[i] == '1':  # 如果当前字符为 1
            queue.append(1)  # 将 1 加入队列
            num_ones += 1    # 将记录 1 的数 +1
            i+=1 
        if num_ones > 0 and num_zero > 0:  # 如果 0 和 1 数量都大于 0 
            res += min(num_zero, num_ones)
            if queue[0] == 0:
                while num_zero > 0:
                    queue.popleft()
                    num_zero -=1
            else:
                while num_ones > 0:
                    queue.popleft()
                    num_ones -=1
    return res


if __name__ == '__main__':
    s = '101001'
    res = main(s)
    print(res)
