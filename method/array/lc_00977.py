# coding=utf-8

def main(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] * nums[i]

    i = 0
    j = len(nums)-1
    # 在原始数组上进行变换
    while i<j:
        if nums[j] >= nums[i]:
            j-=1
        else:
            tt = nums[i]
            nums[i] = nums[j]
            nums[j] = tt
            j-=1

if __name__ == '__main__':
    nums = [-7,-3,2,3,11]
    main(nums)
    print(nums)
