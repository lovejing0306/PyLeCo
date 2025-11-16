# coding=utf-8
import copy

def dfs(nums, start, sum_, target, path, paths):
    if sum_ == target:
        paths.append(copy.deepcopy(path))
        return 
    if sum_ > target:
        return 
    
    for i in range(start, len(nums)):
        if i > start and nums[i] == nums[i-1]:  # 这里的 i 需要大于 start 才能满足去重的效果
            continue
        path.append(nums[i])
        dfs(nums, i+1, sum_ + nums[i], target, path, paths)
        path.pop()


def main(nums, target):
    paths = []

    if len(nums)==0:
        return paths
    
    nums.sort() # 必须排序，排序后才能执行去重

    path = []
    dfs(nums, 0, 0, target, path, paths)
    return paths


if __name__ == '__main__':
    candidates=[2,5,2,1,2]
    target =5

    res = main(candidates, target)
    print(res)
