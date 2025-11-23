# coding=utf-8

def main(nums, target):
    res = []
    if nums is None and len(nums) < 4:
        return res
    
    nums.sort()

    for i in range(len(nums)-3):
        if nums[i] > 0 and nums[i] > target:
            break
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, len(nums)-2):
            if nums[i] + nums[j] > 0 and nums[i] + nums[j] > target: # 剪枝条件
                break
            if j > i+1 and nums[j] == nums[j-1]:
                continue

            tt = target - (nums[i] + nums[j])

            l = j+1
            r = len(nums)-1
            while l < r:
                if nums[l] + nums[r] < tt:
                    l+=1
                    while l<r and nums[l] ==nums[l-1]:
                        l+=1
                elif nums[l] + nums[r] > tt:
                    r-=1
                    while l<r and nums[r] == nums[r+1]:
                        r-=1
                else:
                    res.append([nums[i], nums[j], nums[l], nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l] ==nums[l-1]:
                        l+=1
                    while l<r and nums[r] == nums[r+1]:
                        r-=1
    return res

if __name__ == '__main__':
    nums = [1,0,-1,0,-2,2]
    target = 0
    res = main(nums, target)
    print(res)