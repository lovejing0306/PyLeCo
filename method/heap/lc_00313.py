# coding=utf-8

import heapq

def main(n, primes):
    if n == 1:
        return 1

    heap = []
    heapq.heappush(heap, 1)
    res = []
    visited = {1}
    for _ in range(n):
        val = heapq.heappop(heap)
        res.append(val)
        for prime in primes:
            t = val * prime
            if t in visited:
                continue
            visited.add(t)
            heapq.heappush(heap, t)
    return res[-1]


if __name__ == '__main__':
    n = 12
    primes = [2,7,13,19]
    
