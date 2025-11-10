# coding=utf-8

def main(nums, val):
    # 快慢指针
    i = 0
    j = 0

    while j<len(nums):
        if nums[j] == val:
            tt = nums[i]
            nums[i] = val
            nums[j] = tt
            i+=1
        j+=1
    
    return len(nums) -i


if __name__ == '__main__':
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    res = main(nums, val)
    print(res)
