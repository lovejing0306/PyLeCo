# coding=utf-8
import heapq


def main(flights, n, src, dst, k):
    # 初始化到每个城市的费用为无穷大
    # 记录到每个城市的最小费用
    dist = {i:float('inf') for i in range(n)}
    # 初始化图
    graph = {i: [] for i in range(n)}
    # 将具体的航班信息填写到图中
    for flight in flights:
        s, d, v = flight
        graph[s].append((d, v))
    # 记录在当前时刻，到任意城市的最小费用
    heap = [(0, 0, src)]

    while len(heap) > 0:
        money, num, city = heapq.heappop(heap)
        if num >k:
            continue
        if money > dist[city]:
            continue

        for neighbor, money_ in graph[city]:  # 遍历周围城市
            dist_ = money + money_  # 从当前城市到周围城市的费用
            if dist_ < dist[neighbor]:  # 如果到周围城市的费用小于之前存储的最小费用
                dist[neighbor] = dist_
                heapq.heappush(heap, (dist_, num + 1, neighbor))
    
    if dist[dst] == float('inf'):
        return -1
    else:
        return dist[dst]


if __name__ == '__main__':
    flights = [[0,1,100],[1,2,100],[0,2,500]] # [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
    src = 0  # 0
    dst = 2  # 3
    k = 3  # 1
    n = 3  # 4

    res = main(flights, n, src, dst, k)

    print(res)