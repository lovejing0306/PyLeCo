# coding=utf-8

def main(nums, target):
    # 左闭右闭方案，+1 和 -1 也是跟随着该方案
    res = [-1, -1]

    l = 0
    r = len(nums)-1

    while l <= r:
        m = l + (r-l)//2
        if nums[m] <= target:
            l = m+1
        else:
            r = m-1
    r_ = r

    l = 0
    r = len(nums)-1
    while l<=r:
        m = l + (r-l)//2
        if nums[m] >= target:
            r = m-1
        else:
            l = m+1
   
    if l <= r_:
        res[0] = l
        res[1] = r_
    return res


if __name__ == '__main__':
    nums = [5,7,7,8,8,10]
    target = 5

    res = main(nums, target)
    print(res)
