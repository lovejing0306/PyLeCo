# coding=utf-8

def main(nums):
    if len(nums) <= 1:
        return 0
    
    res = 0
    l = 0  # 左指针
    r = len(nums)-1  # 右指针

    while l<r:   # 两个指针不能重叠
        val = min(nums[l], nums[r])
        area = val * (r-l)  # 计算面积
        res = max(res, area)  # 计算最大值
        # 那个指向的值小，则把那个值往前移动
        if nums[l] <= nums[r]:
            l+=1
        else:
            r-=1
    return res


if __name__ == '__main__':
    nums = [1,8,6,2,5,4,8,3,7]
    res = main(nums)
    print(res)