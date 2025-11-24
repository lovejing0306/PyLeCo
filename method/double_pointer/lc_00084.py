# coding=utf-8
import copy

def method_1(nums):
    """ 
    统计在每种高度下，能够获取到的最大值
    该方案会超时
    """
    hh = copy.deepcopy(nums)
    
    hh.sort()
    max_area = 0

    for i in range(len(hh)):
        h = hh[i]
        if h == 0:
            continue
        if i>0 and hh[i] == hh[i-1]:
            continue
        r = 0
        while r < len(nums):
            if nums[r] >= h:
                l = r
                while r < len(nums) and nums[r] >= h:
                    r+=1
                area = h * (r-l)
                max_area = max(max_area, area)
            else:
                r+=1
    return max_area


def method_2(nums):
    """ 
    对于每根柱子，找到左边第一个小于该柱子的位置，找到右边第一个小于该柱子的位置
    此方案也会超时
    """
    max_v = 0

    for i in range(len(nums)):
        l = i
        while l>=0 and nums[l] >= nums[i]:
            l-=1
        l+=1

        r = i
        while r<=len(nums)-1 and nums[r] >= nums[i]:
            r+=1
        r -= 1
        area = (r-l+1) * nums[i]
        max_v = max(max_v, area)
    return max_v


def method_3(nums):
    """ 
    使用 栈 求解
    """
    n = len(nums)
    stack = []
    max_area = 0
    for i in range(n):
        while stack and nums[stack[-1]] >= nums[i]:  # 如果栈顶元素大于当前元素
            h = nums[stack.pop()]  # 取栈顶元素作为 高
            left = stack[-1] if stack else -1
            w = i - left - 1  # 使用栈顶元素左右相邻的元素位置作为 宽
            if h * w > max_area:
                max_area = h * w
        stack.append(i)
    while stack:
        h = nums[stack.pop()]
        left = stack[-1] if stack else -1
        w = n - left - 1
        if h * w > max_area:
            max_area = h * w
    return max_area


if __name__ == '__main__':
    nums = [2,1,5,6,2,3]
    res = method_2(nums)
    print(res)