# coding=utf-8

def main(nums, target):
    """
    1. 首先，判断 m 落在了哪个区域
    2. 然后，判断目标值在连续区域中的状态
    """
    if len(nums) == 0:
        return -1

    l = 0
    r = len(nums)-1

    while l<=r:
        m = l + (r-l)//2
        if nums[m] == target:
            return m
        elif nums[m] < nums[l]:  # 此条件下 m 落在后半区域
            if nums[m] < target <=nums[r]:  # 判断目标值是否在连续的区域中，连续的区域比较好设置条件
                l = m+1
            else:
                r = m-1
        else:  # 否则 m 落在了前半区域
            if nums[l] <= target < nums[m]:  # 判断目标值是否在连续的区域中，连续的区域比较好设置条件
                r = m-1
            else:
                l = m+1
    return -1


if __name__ == '__main__':
    nums = [4,5,6,7,0,1,2]
    target = 3

    res = main(nums, target)
    print(res)
