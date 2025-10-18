# coding=utf-8

"""
Dijkstra
"""
import heapq

def main(times, n, k):
    """
    times: List[List[int]], n: int, k: int
    """

    # 初始化到节点的最大距离
    dist = {i: float('inf') for i in range(1, n+1)}

    # 构建邻接表
    graph = {i: [] for i in range(n)}
    for time_ in times:
        u, v, w = time_
        graph[u].append((v, w))

    # 优先队列：(当前距离, 节点)
    pq = [(0, k)]  # 到每个节点的距离
    
    # Dijkstra 算法
    while pq:
        current_dist, node = heapq.heappop(pq)  # 从最小堆队列中取最小值
        
        # 如果当前距离大于已记录的距离，跳过
        if current_dist > dist[node]:
            continue
        
        # 遍历所有邻居节点
        for neighbor, weight in graph[node]:   # 广度优优先遍历，先遍历同一层
            distance = current_dist + weight
            
            # 如果找到更短的路径，更新距离
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    # 找出最大距离
    max_dist = max(dist.values())
    
    # 如果有节点无法到达，返回 -1
    return max_dist if max_dist != float('inf') else -1
