# coding=utf-8

import copy

def dfs(nums, visited, path, paths):
    if len(nums) == len(path):
        paths.append(copy.deepcopy(path))
        return
    
    layer_visited = set()  # 这里必须使用 set 方式执行去重复操作
    for i in range(len(nums)):
        # if i > 0 and nums[i]==nums[i-1]:
        #     continue
        if nums[i] in layer_visited:
            continue
        if visited[i]:
            continue
        layer_visited.add(nums[i])
        visited[i] = True
        path.append(nums[i])
        dfs(nums, visited, path, paths)
        visited[i] = False
        path.pop()
    del layer_visited


def main(nums):
    paths = []
    path = []
    visited = {}  # 记录在不同层之间被访问过的索引
    
    for i in range(len(nums)):
        visited[i] = False   # 默认所有节点没有被访问过
    
    dfs(nums, visited, path, paths)
    return paths


if __name__ == '__main__':
    nums = [1,2,1]
    paths = main(nums)
    print(paths)