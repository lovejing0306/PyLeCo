# coding=utf-8

def main(nums):
    max_v = 0

    l = 0
    r = len(nums)-1

    while l < r:
        area = min(nums[l], nums[r]) * (r-l)
        max_v = max(area, max_v)
        if nums[l] < nums[r]:  # 那个指针的值小，则移动那个指针
            l+=1
        else:
            r-=1
    return max_v


if __name__ == '__main__':
    nums = [1,1]
    res = main(nums)
    print(res)