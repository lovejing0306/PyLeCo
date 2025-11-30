# coding=utf-8

def main(nums):
    l = 0
    r = len(nums) - 1
    while l < r:
        m = l + (r - l) // 2
        if nums[m] > nums[m + 1]:
            r = m  # 这里必须把 m 赋值给 r
        else:
            l = m + 1  # 这里必须把 m+1 赋值给 l
    return l


if __name__ == '__main__':
    nums = [1,2,3,1]
    res = main(nums)
    print(res)
