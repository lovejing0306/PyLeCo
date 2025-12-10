# coding=utf-8

import heapq

def main(n):
    if n == 1:
        return 1

    res = []
    heap = []
    heapq.heappush(heap, 1)
    visited = {1}

    for _ in range(n):
        val = heapq.heappop(heap)
        res.append(val)

        for num in [2, 3, 5]:
            t = val * num
            if t in visited:  # 
                continue
            visited.add(t)
            heapq.heappush(heap, t)
    return res[-1]


if __name__ == '__main__':
    n = 10
    res = main(n)
    print(res)