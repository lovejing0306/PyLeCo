# coding=utf-8
import math

def main(nums, k):
    nums.sort()
    
    i = 0 
    while i < len(nums) and k > 0:
        if nums[i] < 0:
            nums[i] =  -nums[i]
            i+=1
            k-=1
        else:
            break
    
    if k > 0 and k %2 == 1:
        nums.sort()
        nums[0] = -nums[0]
    return sum(nums)


if __name__ == '__main__':
    nums = [2,-3,-1,5,-4]
    k = 2
    res = main(nums, k)
    print(res)