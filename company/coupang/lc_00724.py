# coding=utf-8

def main(nums):
    sums = []
    tt = 0
    for num in nums:
        tt += num
        sums.append(tt)

    j = len(nums)-1
    i = 0
    while i<=j:
        a = sums[i]
        b = sums[j] - sums[i] + nums[i]
        if a == b:
            return i
        i+=1
    return -1


if __name__ == '__main__':
    nums = [1, 2, 3]

    res = main(nums)
    print(res)
