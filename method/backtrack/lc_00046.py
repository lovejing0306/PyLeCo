# coding=utf-8

import copy


def dfs(nums, visited, path, paths):
    if len(path) == len(nums):
        paths.append(copy.deepcopy(path))
        return 
    
    for num in nums:
        if visited[num]:
            continue
        visited[num] = True
        path.append(num)
        dfs(nums, visited, path, paths)
        path.pop()
        visited[num] = False


def main(nums):
    paths = []  # 存放符合结果的路径
    path = []   # 存放当前路径上的节点
    visited = {}   # 记录节点被访问的状态，递归过程中，同一条路径上，访问过的节点不会被再次访问，防止排列中出现重复的元素
    for num in nums:
        visited[num] = False
    
    dfs(nums, visited, path, paths)
    return paths


if __name__ == '__main__':
    nums = [1,2,3]
    paths = main(nums)
    print(paths)
