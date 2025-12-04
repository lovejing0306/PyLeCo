# coding=utf-8

def main(nums):
    if not nums:
        return 0

    res = nums[0]  # 全局最大值
    max_prod = nums[0]  # 记录连续子数组的最大值
    min_prod = nums[0]  # 记录连续子数组的最小值

    for i in range(1, len(nums)):
        if nums[i] < 0:  # 关键点，如果当前元素小于 0，需要交换最大值和最小值
            max_prod, min_prod = min_prod, max_prod
        # 从使用和不使用当前元素中取最大值
        max_prod = max(nums[i], max_prod * nums[i])
        # 从使用和不使用当前元素中取最小值
        min_prod = min(nums[i], min_prod * nums[i])
        # 获取全局最大值
        res = max(res, max_prod)
    return res


if __name__ == '__main__':
    nums = [-2,0,-1, -2]
    res = main(nums)
    print(res)
