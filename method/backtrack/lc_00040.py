# coding=utf-8
import copy

def dfs(candidates, target, start_id, sum_, path, paths):
    if sum_ == target:
        paths.append(copy.deepcopy(path))
        return
    if sum_ > target:
        return
    
    for i in range(start_id, len(candidates)):
        if i > start_id and candidates[i] == candidates[i-1]:
            continue
        path.append(candidates[i])
        dfs(candidates, target, i+1, sum_ + candidates[i], path, paths)
        path.pop()


def main(candidates, target):
    path = []
    paths = []
    candidates.sort()   # 在处理同一层去重复的案例中，必须对原始数组进行排序
    
    dfs(candidates, target, 0, 0, path, paths)
    return paths

    
if __name__ == '__main__':
    cc = [10,1,2,7,6,1,5]
    target = 8

    paths = main(cc, target)
    print(paths)
