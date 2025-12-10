# coding=utf-8

import heapq

def method_1(matrix, k):
    """ 
    最坏情况下，空间复杂度可能不符合题意
    """
    m = len(matrix)
    n = len(matrix[0])

    res = []
    min_heap = []
    heapq.heappush(min_heap, (matrix[0][0], 0, 0))

    visited = {(0, 0)}

    while len(min_heap) > 0 and len(res) < k:
        val, i, j = heapq.heappop(min_heap)
        res.append(val)

        if j+1 < n:
            if (i, j+1) not in visited:
                heapq.heappush(min_heap, (matrix[i][j+1], i, j+1))
                visited.add((i, j+1))
        if i+1 < m:
            if (i+1, j) not in visited:
                heapq.heappush(min_heap, (matrix[i+1][j], i+1, j))
                visited.add((i+1, j))
    return res[-1]


def method_2(matrix, k):
    """
    这种写法是 “合并排序列表”
    在有序列表中非常有用
    """
    m = len(matrix)
    n = len(matrix[0])

    res = []
    min_heap = []

    for i in range(m):  # 先把第一列元素信息放入到 最小堆 中
        heapq.heappush(min_heap, (matrix[i][0], i, 0))
    
    while len(min_heap) > 0 and len(res) < k:
        val, i, j = heapq.heappop(min_heap)  # 弹出最小元素
        res.append(val)
        if j + 1 < n: # 访问第 i 行
            heapq.heappush(min_heap, (matrix[i][j+1], i, j+1))
    return res[-1]


if __name__ == '__main__':
    matrix = [[1,5,9],[10,11,13],[12,13,15]]
    k = 8
    # matrix = [[-5]]
    # k = 1
    res = method_2(matrix, k)
    print(res)
