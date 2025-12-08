# coding=utf-8

def main(nums, target):
    res = [-1, -1]

    l = 0
    r = len(nums)-1
    while l<=r:
        m = l + (r-l)//2
        if nums[m] < target:
            l = m+1
        elif nums[m] > target:
            r = m-1
        else:
            if m == 0:
                r=m
                break
            elif nums[m] != nums[m-1]:
                r=m
                break
            else:
                r = m-1
    if r >=0 and nums[r] == target:  # 必须做边界校验
        res[0] = r

    l = 0
    r = len(nums)-1
    while l <=r:
        m = l + (r-l) // 2
        if nums[m] < target:
            l = m+1
        elif nums[m] > target:
            r = m-1
        else:
            if m == len(nums)-1:
                l=m
                break
            elif nums[m] != nums[m+1]:
                l=m
                break
            else:
                l=m+1

    if l < len(nums) and nums[l] == target:  # 必须做边界校验
        res[1] = l
    return res


if __name__ == '__main__':
    # nums = [-1,0,3,5,9,12]
    # target = 9
    nums = [5,7,7,8,8,10]
    target = 4
    res = main(nums, target)
    print(res)
