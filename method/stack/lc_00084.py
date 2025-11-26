# coding=utf-8

def main(nums):
    rr = [len(nums)]*len(nums)  # 记录右边第一个小于当前元素的索引
    ll = [-1] * len(nums)   # 记录左边第一个小于当前元素的索引

    # 从前往后遍历获取右边第一个小于当前元素的索引
    stack = []
    for i in range(len(nums)):
        while len(stack) > 0 and nums[i] < nums[stack[-1]]:
            rr[stack.pop()] = i
        stack.append(i)
    # 从后往前遍历获取左边第一个小于当前元素的索引
    stack = []
    i = len(nums)-1
    while i>=0:
        while len(stack) > 0 and nums[i] < nums[stack[-1]]:
            ll[stack.pop()] = i
        stack.append(i)
        i-=1
    # 计算最大面积
    max_value = 0
    for i in range(len(nums)):
        area = nums[i] * (rr[i] - ll[i] -1)
        max_value = max(max_value, area)
    return max_value


if __name__ == '__main__':
    # nums = [2,1,5,6,2,3]
    nums = [2,4]
    res = main(nums)
    print(res)