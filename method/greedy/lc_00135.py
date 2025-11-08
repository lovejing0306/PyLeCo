# coding=utf-8

def main(nums):
    aa = [0] * len(nums)

    for i in range(1, len(nums)):  # 从左往右遍历
        if nums[i] > nums[i-1]:
            aa[i] = aa[i-1] + 1   # 分配到的糖果数要比前一个大
    
    j = len(nums)-1
    while j>0:    # 从右往左遍历
        if nums[j-1] > nums[j]:
            if aa[j-1] <= aa[j]:
                aa[j-1] = aa[j] + 1
        j-=1
    
    res = sum(aa) + len(nums)
    return res


if __name__ == '__main__':
    ratings = [1,2,2]
    res = main(ratings)
    print(res)