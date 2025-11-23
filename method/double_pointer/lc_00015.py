# coding=utf-8

def main(nums):
    res = []
    if nums is None or len(nums) < 3:
        return res
    
    nums.sort()
    for i in range(len(nums)-2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i-1]:
            continue

        l = i+1
        r = len(nums)-1

        while l < r:
            if nums[l] + nums[r] + nums[i] < 0:
                l+=1
                while l < r and nums[l] == nums[l-1]:
                    l+=1
            elif nums[l] + nums[r] + nums[i] > 0:
                r-=1
                while l < r and nums[r] == nums[r+1]:
                    r-=1
            else:
                res.append([nums[i], nums[l], nums[r]])
                l+=1
                r-=1
                while l < r and nums[l] == nums[l-1]:
                    l+=1
                while l < r and nums[r] == nums[r+1]:
                    r-=1
    return res


if __name__ == '__main__':
    nums = [-1,0,1,2,-1,-4]
    res = main(nums)
    print(res)
