# coding=utf-8

def main(nums):
    i=0
    j=0

    while j<len(nums):
        if nums[j] !=0:
            nums[i] = nums[j]
            i+=1
        j+=1
    while i < len(nums):
        nums[i] = 0
        i+=1
    return nums


if __name__ == '__main__':
    a = [1,2,0,3,0,8]
    main(a)
    print(a)
    