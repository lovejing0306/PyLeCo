# coding=utf-8
import sys

def main(nums):
    max_value = -sys.maxsize-1

    sum_ = 0
    for num in nums:
        sum_ += num
        max_value = max(max_value, sum_)
        if sum_ < 0:
            sum_ = 0  # 如果连续的和小于 0 
    return max_value


if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    res = main(nums)
    print(res)
    