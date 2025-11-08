# coding=utf-8

def main(nums, target):
    l = 0
    r = len(nums)-1

    while l<=r:
        m = l + (r-l)//2
        if nums[m] == target:
            return True
        if nums[l] == nums[m] and nums[m] == nums[r]:  # 关键点1：去除重复元素
            l+=1
            r-=1
            continue
        if nums[m] >= nums[l]:  # 关键点2: 根据左指针 判断 中间指针 落在哪个区间
            if nums[m] > target and target >= nums[l]:
                r = m-1
            else:
                l = m+1
        else:
            if nums[m] < target  and target <= nums[r]:
                l = m+1
            else:
                r= m-1
    return False


if __name__ == '__main__':
    nums = [1, 3, 1, 1, 1]
    target = 3

    res = main(nums, target)
    print(res)
