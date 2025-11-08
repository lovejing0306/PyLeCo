# coding=utf-8

def main(nums, fee):
    if len(nums) <=1 :
        return 0

    count = 0
    min_value = nums[0]
    for i in range(1, len(nums)):
        min_value = min(min_value, nums[i])
        if nums[i] - min_value > fee:
            count += (nums[i]-min_value-fee)
            min_value = nums[i] - fee   # 这个地方不好理解
    return count


if __name__ == '__main__':
    prices = [1,3,7,5,10,3]
    fee = 3

    res = main(prices, fee)
    print(res)
