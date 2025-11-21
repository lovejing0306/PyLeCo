# coding=utf-8

def main(nums):
    counter = [0] * 101

    for num in nums:
        counter[num] += 1
    
    sums = [0] * 101

    sum_ = 0
    for i in range(len(counter)):
        sum_ += counter[i]
        sums[i] = sum_
    
    res = []
    for num in nums:
        if num == 0:
            res.append(0)
        else:
            res.append(sums[num-1])
    return res


if __name__ == '__main__':
    nums = [7,7,7,7]
    res = main(nums)
    print(res)