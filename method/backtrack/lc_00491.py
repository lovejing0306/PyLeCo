# coding=utf-8

import copy


def dfs(nums, start_id, path, paths):
    if len(path) >1:
        paths.append(copy.deepcopy(path))
    if len(nums) == start_id:
        return
    
    tt = set()
    for i in range(start_id, len(nums)):
        if nums[i] in tt:
            continue
        if len(path) == 0:
            path.append(nums[i])
        else:
            if path[-1] <= nums[i]:
                path.append(nums[i])
            else:
                continue
        dfs(nums, i+1, path, paths)
        path.pop()
        tt.add(nums[i])
    del tt


def main(nums):
    path = []
    paths = []
    dfs(nums, 0, path, paths)
    return paths


if __name__ == '__main__':
    nums = [4,6,7,7]
    paths = main(nums)

    print(paths)
