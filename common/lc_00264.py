# coding=utf-8
import heapq

def main(n):
    if n == 1:
        return 1
    
    res = []
    visited = set()
    heap = []
    heapq.heappush(heap, 1)
    while len(res) < n:
        a = heapq.heappop(heap)
        res.append(a)
        x1 = a * 2
        x2 = a * 3
        x3 = a * 5

        if x1 not in visited:
            heapq.heappush(heap, x1)
            visited.add(x1)
        if x2 not in visited:
            heapq.heappush(heap, x2)
            visited.add(x2)
        if x3 not in visited:
            heapq.heappush(heap, x3)
            visited.add(x3)
    return res[-1]


if __name__ == '__main__':
    n = 10
    print(main(n))
