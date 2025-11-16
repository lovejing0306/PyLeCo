# coding=utf-8

def main(nums):
    if len(nums) <= 1:
        return len(nums)
    l = 0  # 维护一个变量替换的指针
    count = 1   # 统计重复数组的数量
    for r in range(1, len(nums)):
        if nums[r] == nums[r-1]:
            count +=1
        else:
            ll = min(count, 2)
            for _ in range(ll):
                nums[l] = nums[r-1]
                l+=1
            count = 1
    # 做最后的判断
    ll = min(count, 2)
    for _ in range(ll):
        nums[l] = nums[-1]
        l+=1
    return l


if __name__ == '__main__':
    nums = [0,0,1,1,1,1,2,3,3]
    res = main(nums)
    print(res)