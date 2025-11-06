# coding=utf-8

def main(nums):
    """
    本质上求 单调区间
    """

    if len(nums) == 1:
        return 1

    count = 0
    i = 0   # i 记录区间的左端点
    j = 1   # j 表示探索区间的指针

    while j < len(nums):
        while j < len(nums) and nums[j-1] <=nums[j]:  # 判断是否是递增区间
            j+=1
        if j>1 and nums[j-1] > nums[i]:  # 如果 j>1，说明 j 发生了移动，说明是递增区间
            count+=1
            i = j-1
        if j>=len(nums):  # 提前结束循环
            break

        while j < len(nums) and nums[j-1] >= nums[j]:   # 判断是否是递减区间
            j+=1
        if nums[j-1] < nums[i]:  # 判断是否真的是一个递减区间
            count +=1
            i = j-1
        if j >= len(nums):
            break
    return count +1


if __name__ == '__main__':
    nums = [1,7,4,9,2,5]
    res = main(nums)
    print(res)
