# coding=utf-8

def main(nums):
    maxReach = 0  # 记录最远能够达到的索引
    for i, step in enumerate(nums):
        if i > maxReach:  # 如果当前下标大于最远能够达到的下标，则返回 False
            return False
        maxReach = max(maxReach, i + step)
        if maxReach >= len(nums) - 1:
            return True
    return True


if __name__ == '__main__':
    nums = [3,2,1,0,4]
    res = main(nums)
    print(res)