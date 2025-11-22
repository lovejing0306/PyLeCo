# coding=utf-8

def main(nums, target):
    if nums is None or len(nums) < 4:
        return []

    nums.sort()  # 必须排序，方便去重
    
    res = []
    for i in range(len(nums)-3):
        # if nums[i] > target:  # 当 nums[i] 为负数时不正确，只有当 nums[i] > 0 时才正确 
        #     break
        if nums[i] > 0 and nums[i]>target:  # 注意这里的剪枝方式
            break
        if i > 0 and nums[i]==nums[i-1]:  # 执行去重
            continue
        for j in range(i+1, len(nums)-2):  
            if nums[i] + nums[j] > 0 and nums[i] + nums[j] > target:  # 注意这里的剪枝方式
                break
            if j > i+1 and nums[j] == nums[j-1]: # 执行去重
                continue

            tt = target-(nums[i] + nums[j])
            l = j + 1
            r = len(nums)-1

            while l < r:
                if nums[l] + nums[r] < tt:
                    l+=1
                    while l < r and nums[l] == nums[l-1]:  # 执行去重
                        l+=1
                elif nums[l] + nums[r] > tt:
                    r-=1
                    while l<r and nums[r] == nums[r+1]:  # 执行去重
                        r-=1
                else:
                    res.append([nums[i], nums[j], nums[l], nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l-1]:  # 执行去重
                        l+=1
                    while l<r and nums[r] == nums[r+1]:  # 执行去重
                        r-=1
    return res


if __name__ == '__main__':
    # nums = [1,0,-1,0,-2,2]
    # target = 0
    nums = [2,2,2,2,2]
    target = 8
    res = main(nums, target)
    print(res)