# coding=utf-8

def method_1(nums):
    if nums is None or len(nums) < 3:
        return []

    nums.sort()  # 去重，必须排序
    res = []

    for i in range(len(nums)-2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i-1]:
            continue

        l = i + 1
        r = len(nums)-1
        while l < r:
            if nums[l] + nums[r] > -nums[i]:
                r-=1
                while l < r and nums[r] == nums[r+1]:
                    r-=1
            elif nums[l] + nums[r] < -nums[i]:
                l += 1
                while l < r and nums[l] == nums[l-1]:
                    l+=1
            else:
                res.append([nums[i], nums[l], nums[r]])
                l+=1
                r-=1
                while l < r and nums[l] == nums[l-1]:
                    l+=1
                while l < r and nums[r] == nums[r+1]:
                    r-=1
            
    return res


def method_2(nums):
    if nums is None or len(nums) < 3:
        return []
    nums.sort()  # 去重，必须排序
    res = []
    for i in range(len(nums)-2):
        if nums[i] > 0:
            break
        if i> 0 and nums[i] == nums[i-1]:
            continue
        target = -nums[i]

        his = set()  # 使用 哈希表
        j = i+1
        while j < len(nums):
            diff = target - nums[j]
            if diff in his:
                his.add(nums[j])  # 先把当前元素加入 哈希表
                res.append([nums[i], nums[j], diff])
                j+=1
                # 如果有满足条件的结果，则执行去重
                while j < len(nums) and nums[j] == nums[j-1]:
                    j+=1
            else:
                his.add(nums[j])  # 先把当前元素加入 哈希表
                j+=1
    return res


if __name__ == '__main__':
    # nums = [-1,0,1,2,-1,-4]
    nums = [0,0,0]
    res = method_2(nums)
    print(res)
