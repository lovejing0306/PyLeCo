# coding=utf-8

def dfs(nums, path, paths, visited):
    if len(path) == len(nums):
        paths.append([path[:]])
        return
    
    for i in range(len(nums)):
        if visited[i]:
            continue
        visited[i] = True
        path.append(nums[i])
        dfs(nums, path, paths, visited)
        path.pop()
        visited[i] = False

def permute(nums):
    path = []
    paths = []
    visited = [False] * len(nums)
    dfs(nums, path, paths, visited)
    for path in paths:
        print(path)


def main(nums):
    if len(nums) == 1:
        return nums
    
    flag = -1
    i = len(nums)-1
    while i >= 0:
        j = len(nums)-1  # 每次从最后一个数开始，遍历到 i 之前
        while j > i:
            if nums[j] > nums[i]:
                t = nums[i]
                nums[i] = nums[j]
                nums[j] = t
                flag = i  # 将 i 之后的数字做排序
                break
            j-=1
        i-=1
        if flag !=-1:
            break
    
    nums_ = nums[flag+1:]
    nums_.sort()

    for i in range(flag+1, len(nums)):
        nums[i] = nums_[i-flag-1]
    return nums


if __name__ == '__main__':
    nums = [1,3,5,4,2]
    # permute(nums)
    res = main(nums)
    print(res)