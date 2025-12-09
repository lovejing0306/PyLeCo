# coding=utf-8

def main(nums):
    l = 0
    r = len(nums)-1

    max_val = 0
    while l < r:
        area = (r-l) * min(nums[l], nums[r])
        max_val = max(area, max_val)
        if nums[l] < nums[r]:
            l+=1
        else:
            r-=1
    return max_val

if __name__ == '__main__':
    nums = [1,1]
    res = main(nums)
    print(res)