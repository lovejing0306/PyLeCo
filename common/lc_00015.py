# coding=utf-8

def main(nums):
    res = []
    if len(nums) < 3:
        return res

    nums.sort()  # 必须排序
    
    for i in range(len(nums)-2):
        # 执行去重复
        if i > 0 and nums[i] == nums[i-1]:
            continue
        # 如果元素大于 0，必定不存在 3 数之和为 0，直接跳出
        if nums[i] > 0:
            break
        # 设置目标值
        target = -nums[i]

        l = i+1   # 设置左指针
        r = len(nums) - 1   # 设置右指针

        while l < r:
            sum_ = nums[l] + nums[r]  # 左右指针之和
            if sum_ > target:
                r-=1
                # 执行去重
                while l < r and nums[r] == nums[r+1]:
                    r-=1
            elif sum_ < target:
                l+=1
                # 执行去重
                while l<r and nums[l] == nums[l-1]:
                    l+=1
            else:
                res.append([nums[i], nums[l], nums[r]])
                # 执行去重
                l+=1
                while l<r and nums[l] == nums[l-1]:
                    l+=1
                r-=1
                while l < r and nums[r] == nums[r+1]:
                    r-=1
    return res


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    res = main(nums)
    print(res)
