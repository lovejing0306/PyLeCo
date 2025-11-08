# coding=utf-8

def main(nums, target):
    # 采用 闭区间 方案，结果在区间 [l, r] 中
    l = 0
    r = len(nums)-1

    while l <= r:
        m = l + (r-l)//2
        if nums[m] > target:
            r = m-1
        elif nums[m] < target:
            l = m+1
        else:
            return m
    print(l, r)
    return -1


if __name__ == '__main__':
    nums = [-1,0,3,5,9,12]
    t = 4
    res = main(nums, t)
    print(res)