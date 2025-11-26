# coding=utf-8

import heapq

def main(nums, k):
    counter = {}

    for num in nums:
        if num in counter:
            counter[num] += 1
        else:
            counter[num] = 1
    
    res = []
    if len(counter) <= k:
        res = list(counter.keys())
    else:
        tt = []
        i = 0
        for key, value in counter.items():
            heapq.heappush(tt, (-value, i, key))
            i+=1
        i = 0
        while i<k:
            _, _, key = heapq.heappop(tt)
            res.append(key)
            i+=1
    return res

if __name__ == '__main__':
    nums = [1,2,1,2,1,2,3,1,3,2]
    k = 2
    res = main(nums, k)
    print(res)
