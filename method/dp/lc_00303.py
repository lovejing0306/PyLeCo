# coding=utf-8

from collections import List

class NumArray:
    def __init__(self, nums: List[int]):
        sums = []
        sum_ = 0
        for num in nums:
            sum_ += num
            sums.append(sum_)
        self.sums = sums
        self.nums = nums
        
    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right] - self.sums[left] + self.nums[left]