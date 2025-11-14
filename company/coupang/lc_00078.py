# coding=utf=8
import copy

def dfs(nums, s, path, paths):
    paths.append(copy.deepcopy(path))  # 这里需要执行深度拷贝
    if s == len(nums):
        return
    for i in range(s, len(nums)):
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
    res = main(nums)
    print(res)
