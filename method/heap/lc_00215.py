# coding=utf-8

import heapq
import random

def method_1(nums, k):
    """ 
    使用 堆排序，总时间复杂度为 O(n log k)
    """
    heap = []
    for i in range(len(nums)):
        if i < k:
            heapq.heappush(heap, nums[i])
        else:
            val = heapq.heappop(heap)
            if val < nums[i]:
                heapq.heappush(heap, nums[i])
            else:
                heapq.heappush(heap, val)
    res = heapq.heappop(heap)
    return res


def method_2(nums, k):
    """ 
    使用快速排序，平均时间复杂度为 O(n)
    1. 第 k 个最大的元素 = 第 (n-k) 个最小的元素
    2. 使用快速选择算法，每次选择一个基准元素进行分区
    3. 根据基准位置决定在左边还是右边继续查找
    4. 平均时间复杂度 O(n)，最坏 O(n²)，可通过随机化优化
    """
    target = len(nums) - k
    left, right = 0, len(nums) - 1

    while left <= right:
        p = random.randint(left, right)
        pivot = nums[p]
        nums[p], nums[right] = nums[right], nums[p]
        lt = left
        i = left
        gt = right
        while i <= gt:
            if nums[i] < pivot:
                nums[lt], nums[i] = nums[i], nums[lt]
                lt += 1
                i += 1
            elif nums[i] > pivot:
                nums[gt], nums[i] = nums[i], nums[gt]
                gt -= 1
            else:
                i += 1
        if target < lt:
            right = lt - 1
        elif target > gt:
            left = gt + 1
        else:
            return nums[target]


if __name__ == '__main__':
    # nums = [3,2,1,5,6,4]
    # k = 2
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    res = method_2(nums, k)
    print(res)