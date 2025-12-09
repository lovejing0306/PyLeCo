# coding=utf-8

def main(nums):
    slow = 0
    fast = 0
    res = 0
    while fast < len(nums):
        count = 0  # 记录每个数字重复的次数
        j = fast   # 计算数字重复的次数
        while j<len(nums) and nums[j] == nums[fast]:
            count +=1
            j+=1
        # 数字最多出现两次
        count = min(count, 2)
        res += count  # 记录符合条件的数字出现次数
        while count > 0:  # 将数字的值赋值给慢指针
            nums[slow] = nums[fast]
            slow += 1
            count -=1
        fast = j
    return res


if __name__ == '__main__':
    # nums = [1,8,6,2,5,4,8,3,7]
    nums = [0,0,1,1,1,1,2,3,3]
    res = main(nums)
    print(res)