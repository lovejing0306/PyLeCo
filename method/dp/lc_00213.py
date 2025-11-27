# coding=utf-8

def main(nums):
    """
    对于有环的 DP 问题需要将环解开，需要分两种情况讨论：
    不偷第一个房子：可以考虑偷 [1, n-1] 范围的房子
    不偷最后一个房子：可以考虑偷 [0, n-2] 范围的房子
    """
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])
    
    dp_0 = [0] * len(nums)
    dp_0[0] = 0
    dp_0[1] = nums[1]
    for i in range(2, len(dp_0)):
        dp_0[i] = max(dp_0[i-1], dp_0[i-2] + nums[i])
    
    dp_1 = [0] * len(nums)
    dp_1[0] = nums[0]
    dp_1[1] = max(nums[0], nums[1])
    for i in range(2, len(dp_1)-1):
        dp_1[i] = max(dp_1[i-1], dp_1[i-2] + nums[i])
    
    return max(dp_0[-1], dp_1[-2])


if __name__ == '__main__':
    nums = [5, 1, 3, 9]
    res = main(nums)
    print(res)
