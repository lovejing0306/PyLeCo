# coding=utf-8

def main(nums, val):
    if nums is None or len(nums)==0:
        return 0

    l = 0
    r = 0

    while r < len(nums):
        if nums[r]==val:
            r+=1
        else:
            nums[l] = nums[r]
            l+=1
            r+=1
    return l

if __name__ == '__main__':
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    res = main(nums, val)
    print(res)