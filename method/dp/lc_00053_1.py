# coding=utf-8

def main(nums):
    max_g = nums[0]  # 全局最大值
    max_l = nums[0]  # 局部最大值

    for i in range(1, len(nums)):
        max_l = max(max_l + nums[i], nums[i])
        max_g = max(max_g, max_l)
    return max_g

if __name__ == '__main__':
    nums = [5,4,-1,7,8]
    res = main(nums)
    print(res)
