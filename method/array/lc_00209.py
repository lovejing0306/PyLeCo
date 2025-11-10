# coding=utf-8
import sys

def main(nums, target):
    i = 0
    j = 0
    sum_ = 0
    min_v = sys.maxsize

    while j < len(nums):
        sum_ += nums[j]
        j += 1
        while sum_>= target:
            min_v = min(min_v, j-i) 
            sum_ -= nums[i]
            i+=1
        
    return 0 if min_v == sys.maxsize else min_v

if __name__ == '__main__':
    nums = [1,4,4]
    tt = 4
    res = main(nums, tt)
    print(res)
