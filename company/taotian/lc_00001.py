# coding=utf-8

def main(nums):
    """ 
    最大子数组的和，带返回的起始和结束索引
    """
    
    cur_sum = nums[0]
    max_sum = nums[0]

    start = 0
    max_s = 0
    max_e = 0

    for i in range(1, len(nums)):
        cur_sum += nums[i]
        if cur_sum <= nums[i]:
            cur_sum = nums[i]
            start = i   # 记录新序列的临时起点
        if cur_sum > max_sum:
            max_sum = cur_sum
            # 同时 更新最大序列的 新起点和结束点
            max_s = start
            max_e = i
    
    return max_sum, max_s, max_e


if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    res = main(nums)
    print(res)