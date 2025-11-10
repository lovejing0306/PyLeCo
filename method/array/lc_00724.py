# coding=utf-8

def main(nums):
    sums = []
    sum_ = 0

    for i in range(len(nums)):
        sum_+=nums[i]
        sums.append(sum_)
    
    for i in range(len(nums)):
        a = sums[i]
        b = sums[len(nums)-1]-sums[i] + nums[i]
        if a == b:
            return i
    return -1


if __name__ == '__main__':
    nums = [2, 1, -1]
    res = main(nums)
    print(res)
