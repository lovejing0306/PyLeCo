# coding=utf-8

def main(nums):
    if len(nums) <=1:
        return 0

    max_index = 0
    # 找到最大值对应的索引
    for i in range(1, len(nums)):
        if nums[i] > nums[max_index]:
            max_index = i
    res = 0
    # 从前往后到最大值索引
    l = 0
    cur_index = 0

    while l<max_index:
        if nums[l] > nums[cur_index]:
            cur_index = l
        else:
            res += (nums[cur_index]-nums[l])
        l+=1
    # 从后往前到最大值索引
    r = len(nums)-1
    cur_index = r
    while r > max_index:
        if nums[r] > nums[cur_index]:
            cur_index = r
        else:
            res += (nums[cur_index]-nums[r])
        r-=1
    
    return res


if __name__ == '__main__':
    nums = [4,2,0,3,2,5]
    res = main(nums)
    print(res)
