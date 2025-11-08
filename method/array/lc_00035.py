# coding=utf-8

def main(nums, target):

    l = 0
    r = len(nums)-1
    m = -1
    while l<=r:
        m = l + (r-l)//2
        if nums[m] < target:
            l = m+1
        elif nums[m] > target:
            r = m-1
        else:
            return m
    return l  # 在 left 位置插入


if __name__ == '__main__':
    nums = [1,3,5,6]
    target = 0

    res = main(nums, target)
    print(res)
