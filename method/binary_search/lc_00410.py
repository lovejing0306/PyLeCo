# coding=utf-8

def is_valid(k, nums, max_sum):
    count = 1    # 当前子数组个数
    cur_sum = 0  # 当前子数组的和

    for num in nums:
        cur_sum += num
        if cur_sum > max_sum:  # 如果子数组的和大于最大值
            count +=1
            cur_sum = num  # 用当前值重置子数组的和
    return count <= k


def main(nums, k):
    # 定义二分查找的范围
    l = max(nums)  # 最小可能值：数组中的最大元素
    r = sum(nums)  # 最大可能值：所有元素的和

    while l < r:
        m = l + (r-l) // 2
        if is_valid(k, nums, m): # 如果 m 值可行，尝试更小的 m 值
            r = m
        else:
            l = m+1
    return l
    

if __name__ == '__main__':
    # nums = [7,2,5,10,8]
    # k = 2
    nums = [1,2,3,4,5]
    k = 2
    res = main(nums, k)
    print(res)