# coding=utf-8

import copy

def dfs(nums, start_id, path, paths):
    paths.append(copy.deepcopy(path))
    if len(nums) == start_id:
        return
    
    for i in range(start_id, len(nums)):
        path.append(nums[i])
        dfs(nums, i+1, path, paths)
        path.pop()


def main(nums):
    path = []
    paths = []
    dfs(nums, 0, path, paths)
    return paths


if __name__ == '__main__':
    nums = [1,2,3]
    paths = main(nums)
    print(paths)
