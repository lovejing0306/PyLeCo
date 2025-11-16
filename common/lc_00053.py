# coding=utf-8

def main(nums):
    max_val = nums[0]
    
    ss = nums[0]
    for num in nums[1:]:
        ss += num
        if num >= ss:
            ss = num
        max_val = max(max_val, ss)
    return max_val

if __name__ == '__main__':
    nums = [-1]
    res = main(nums)
    print(res)