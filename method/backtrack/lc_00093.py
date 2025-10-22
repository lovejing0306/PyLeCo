# coding=utf-8

import copy

def is_valid(s):
    if len(s) > 1 and s[0] == '0':
        return False
    if int(s) > 255:
        return False
    return True


def dfs(ss, start_id, path, paths):
    if len(path)>4:
        return 
    if len(ss) < start_id:
        return
    if len(ss) == start_id and len(path)==4:
        paths.append('.'.join(copy.deepcopy(path)))
        return
    
    
    for i in range(start_id, len(ss)):
        s = ss[start_id: i+1]
        if is_valid(s):
            path.append(s)
        else:
            continue
        dfs(ss, i+1, path, paths)
        path.pop()


def main(ss):
    """
    和分割回文串如出一辙
    """
    path = []
    paths = []

    dfs(ss, 0, path, paths)

    return paths


if __name__ == '__main__':
    ss = '101023'  # 101023
    paths = main(ss)

    print(paths)
