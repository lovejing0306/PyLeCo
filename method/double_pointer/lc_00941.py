# coding=utf-8

def main(nums):
    if nums is None or len(nums) < 3:
        return False

    max_index = 0
    for i in range(len(nums)):
        if nums[i] > nums[max_index]:
            max_index = i
    
    if max_index == 0 or max_index == len(nums)-1:
        return False
    
    l = 0
    while l < max_index:
        if nums[l] < nums[l+1]:
            l+=1
        else:
            return False
    
    r = len(nums) - 1
    while r > max_index:
        if nums[r] < nums[r-1]:
            r-=1
        else:
            return False
    
    return True
    

if __name__ == '__main__':
    nums = [0,3,2,1]
    res = main(nums)
    print(res)