# coding=utf-8

import heapq

def main(grid):
    m = len(grid)
    n = len(grid[0])
    # 每个节点可以遍历的上下左右方向
    dire = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    res = []
    min_heap = []   # 最小堆
    visited = {(0, 0)}  # 记录节点是否被访问过
    # 将左上角的元素放入到 最小堆 中
    heapq.heappush(min_heap, (grid[0][0], 0, 0 ))

    while len(min_heap) > 0:  # 访问最小堆
        val, i, j = heapq.heappop(min_heap)  # 弹出最小值
        res.append(val)
        if i == m-1 and j == n-1:  # 如果访问到了末尾元素，则直接跳出
            break
        for item in dire:
            x = i + item[0]
            y = j + item[1]
            # 如果新的节点在边界内，同时没有被访问过
            if 0<= x <m and 0<=y < n and (x, y) not in visited:
                heapq.heappush(min_heap, (grid[x][y], x, y))
                visited.add((x, y))  # 加入到已经访问过的列表
    return max(res)


if __name__ == '__main__':
    # grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
    grid = [[0,2],[1,3]]
    res = main(grid)
    print(res)