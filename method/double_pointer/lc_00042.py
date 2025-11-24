# coding=utf-8

def main(nums):
    if nums is None or len(nums) <= 1:
        return 0
    
    max_index = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[max_index]:
            max_index = i
    
    count = 0
    l = 0
    i = 0
    while i < max_index:
        if nums[i] <= nums[l]:
            count += (nums[l] - nums[i])
        else:
            l = i
        i+=1

    r = len(nums)-1
    j = len(nums)-1

    while j > max_index:
        if nums[j] <= nums[r]:
            count += (nums[r]-nums[j])
        else:
            r = j 
        j-=1
    return count


if __name__ == '__main__':
    nums = [4,2,0,3,2,5]
    res = main(nums)
    print(res)