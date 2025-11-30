# coding=utf-8

def main(nums, target):
    n = len(nums)
    res = [-1, -1]

    l = 0
    r = n - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] >= target:
            r = m - 1
        else:
            l = m + 1
    if l < n and nums[l] == target:
        res[0] = l
    else:
        return res

    l = 0
    r = n - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] <= target:
            l = m + 1
        else:
            r = m - 1
    res[1] = r
    return res


if __name__ == '__main__':
    # a = [1,1,1,2,2,6,7]
    a = [5,7,7,8,8,10]
    target = 8
    print(main(a, target))