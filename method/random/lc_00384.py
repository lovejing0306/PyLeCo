# coding=utf-8
import random

class Solution:
    def __init__(self, nums):
        self.org = nums[:]
        self.arr = nums[:]

    def reset(self):
        self.arr = self.org[:]
        return self.arr

    def shuffle(self,):
        """ 
        洗牌算法 - Fisher-Yates (Knuth) 算法
        从后向前遍历数组
        对于位置 i，从 [0, i] 范围内随机选择一个位置 j
        交换 nums[i] 和 nums[j]
        """
        for i in range(len(self.arr)-1, 0, -1):
            j = random.randint(0, i)
            self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        return self.arr

if __name__ == '__main__':
    pass
