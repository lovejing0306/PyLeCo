# coding=utf-8

import heapq

def method_1(nums1, nums2, k):
    """
    这种方案会超时
    """
    heap = []
    count = 0
    for num1 in nums1:
        for num2 in nums2:
            if len(heap) < k:
                heapq.heappush(heap, (-(num1 + num2), count, num1, num2))
            else:
                if -heap[0][0] > (num1+num2):
                    heapq.heappop(heap)
                    heapq.heappush(heap, (-(num1 + num2), count, num1, num2))
            count += 1
    
    res = []
    for item in heap:
        res.append([item[-2], item[-1]])
    return res

def method_2(nums1, nums2, k):
    if nums1 is None or nums2 is None:
        return []
    # 最小堆：存储 (和, nums1的索引, nums2的索引)
    min_heap = []
    for i in range(min(k, len(nums1))):
        heapq.heappush(min_heap, (nums1[i]+nums2[0], i, 0))
    
    res = []
    # 取出 k 个最小的配对
    while min_heap and len(res) < k:
        _, i, j = heapq.heappop(min_heap)
        # 如果 nums2 还有下一个元素，将新配对加入堆
        res.append([nums1[i], nums2[j]])
        if j + 1 < len(nums2):
            heapq.heappush(min_heap, (nums1[i] + nums2[j+1], i, j+1))
    return res

    
if __name__ == '__main__':
    nums1 = [1,7,11]
    nums2 = [2,4,6]
    k = 3
    # nums1 = [1,1,2]
    # nums2 = [1,2,3]
    # k = 2
    res = method_2(nums1, nums2, k)
    print(res)