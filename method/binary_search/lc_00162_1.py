# coding=utf-8

def main(nums):
    if len(nums) == 1:
        return 0
    
    l = 0
    r = len(nums)-1

    while l <= r:
        m = l + (r-l) // 2
        if m == 0:
            if nums[m] > nums[m+1]:
                return m
            else:
                l = m+1
        elif m == len(nums)-1:
            if nums[m] > nums[m-1]:
                return m
            else:
                r = m-1
        elif nums[m-1]  < nums[m] > nums[m+1]:
            return m
        elif nums[m] < nums[m-1]:
            r = m-1
        elif nums[m] < nums[m+1]:
            l = m+1
    return -1


if __name__ == '__main__':
    nums = [1,2,3,1]
    res = main(nums)
    print(res)
