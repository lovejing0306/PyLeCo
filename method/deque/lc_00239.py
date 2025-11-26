# coding=utf-8
from collections import deque

def main(nums, k):
    """
    始终保持队列的首元素对应的是当前窗口的最大值
    """
    if len(nums) <=k:   # 如果窗口大小大于等于数组的长度，则直接返回数组种的最大值
        return [max(nums)]
    
    res = []
    queue = deque()   # 构建双端对列
    for i in range(len(nums)):  
        if i < k:  # 考虑前 k 个元素
            # 如果队尾元素的值小于当前元素的值，则把队尾元素的值弹出
            while len(queue) > 0 and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i) # 将当前索引加入到 队列中
            if i == k-1:  # 如果当前索引等于窗口大小
                res.append(nums[queue[0]])  # 取出队列的首元素
        else:
            start = i - k + 1   # 窗口的起始索引
            # 如果队列首元素不在窗口区间，则弹出队首元素
            while len(queue) > 0 and queue[0] < start:  
                queue.popleft()
            # 如果队列尾元素小于当前元素，则弹出队尾元素
            while len(queue) > 0 and nums[queue[-1]] < nums[i]:  
                queue.pop()
            queue.append(i)  # 将当前索引加入到 队列中
            res.append(nums[queue[0]])
    return res


if __name__ == '__main__':
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3

    res = main(nums, k)
    print(res)