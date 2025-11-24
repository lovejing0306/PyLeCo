# coding=utf-8

def main(nums, k):
    k = k % len(nums)

    nums.reverse()

    l = 0
    r = k-1
    while l<r:
        t = nums[l]
        nums[l] = nums[r]
        nums[r] = t
        l+=1
        r-=1
    
    l = k
    r = len(nums)-1
    while l<r:
        t = nums[l]
        nums[l] = nums[r]
        nums[r] = t
        l+=1
        r-=1
    return nums


if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7]
    k = 3
    res = main(nums, k)
    print(res)
