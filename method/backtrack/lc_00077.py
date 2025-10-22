# coding=utf-8

import copy

def dfs(start_id, n, k, path, paths):
    if len(path) == k:
        paths.append(copy.deepcopy(path))
        return 
    if n - start_id + 1 < k - len(path):  # 如果剩余元素的数量无法构成 k 个元素组成的集合，则跳过
        return

    for i in range(start_id, n+1):
        path.append(i)
        dfs(i+1, n, k, path, paths)
        path.pop()

def main(n, k):
    path = []
    paths = []
    dfs(1, n, k, path, paths)
    return paths


if __name__ == '__main__':
    paths = main(4, 2)
    print(paths)