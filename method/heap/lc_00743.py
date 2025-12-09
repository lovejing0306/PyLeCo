# coding=utf-8
import heapq

def main(times, n, k):
    nums = [-1] * (n+1)  # 记录到每个节点的距离
    
    mapping = {}  
    for time_ in times:  # 构建邻接矩阵
        node1, node2, val = time_
        if node1 in mapping:
            mapping[node1].append((node2, val))
        else:
            mapping[node1] = [(node2, val)]
    
    visited = set()  # 记录已经访问过的点
    total = 0  # 记录点的数量
    heap = []   # 最小堆
    heapq.heappush(heap, (0, total, k))

    while len(heap) > 0:
        # 从堆中取出 最短距离的 节点
        path_len, _, node1 = heapq.heappop(heap)
        # 如果当前节点已经访问过，则跳过
        if node1 in visited:
            continue
        # 如果当前没有被访问过，将当前节点标记为访问状态
        visited.add(node1)
        # 记录到当前节点的路径
        nums[node1] = path_len
        for item in mapping.get(node1, []):  # 访问该节点能够达到的子节点
            node2, val = item
            if node2 in visited:  # 如果子节点已经被访问过，则跳过
                continue
            total +=1  
            heapq.heappush(heap, (path_len + val, total, node2))  # 将子节点加入到堆中
    max_val = 0
    # 访问每个节点
    for num in nums[1:]:
        if num == -1:  # 如果有 -1，说明有的节点没有到达，直接返回 -1
            return -1
        max_val = max(max_val, num)
    return max_val
    

if __name__ == '__main__':
    # times = [[2,1,1],[2,3,1],[3,4,1]]
    # n = 4
    # k = 2
    times = [[1,2,1]]
    n = 2
    k = 1
    res = main(times, n, k)
    print(res)