# coding=utf-8

def convert(n):
    nums = []
    while n > 0:
        a = n % 10
        n = n // 10
        nums.append(a)
    nums.reverse()
    return nums

def merge(nums):
    i = len(nums)-1
    sum_ = 0
    acc = 1
    while i >= 0:
        sum_ += nums[i] * acc
        acc *= 10
        i-=1
    return sum_


def main(n):
    if n < 10:
        return n
    nums = convert(n)
    
    i = 1
    while i < len(nums):   # 从前往后遍历，找到第一个递减的地方
        if nums[i-1] <= nums[i]:
            pass
        else:
            nums[i-1] -= 1
            for j in range(i, len(nums)):  # 从递减位置开始，将后面所有元素值都赋值为 9
                nums[j] = 9
            break
        i += 1
    
    i-=1
    while i>0:  # 递减位置开始，往前遍历
        if nums[i-1] > nums[i]:  # 判断是否是递减序列
            nums[i] = 9
            nums[i-1] -= 1
        i-=1
    
    res = merge(nums)
    return res


if __name__ == '__main__':
    n = 10
    res = main(n)
    print(res)