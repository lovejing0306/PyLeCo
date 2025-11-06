# coding=utf-8
from collections import deque


def main(ss):
    r = deque()
    d = deque()
    n = len(ss)

    for i in range(len(ss)):
        if ss[i] == 'R':
            r.append(i)
        else:
            d.append(i)
    
    while r and d:
        # 这里有个巧妙的点，同时做了 弹出 相当于做了删除
        r_index = r.popleft()
        d_index = d.popleft()
        # 位置靠前的参议员获胜，禁止另一方
        if r_index > d_index:
            r.append(r_index + n)    # 加n表示下一轮
        else:
            d.append(d_index + n)
    return 'Radiant' if r else 'Dire'


if __name__ == '__main__':
    senate = "RDDR"
    res = main(senate)
    print(res)
