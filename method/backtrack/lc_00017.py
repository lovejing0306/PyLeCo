# coding=utf-8

import copy


def dfs(ss, num2string, c_id, path, paths):
    if len(ss) == c_id:  # 如果访问到最后一个字符串时，则返回
        paths.append(''.join(copy.deepcopy(path)))
        return
    tt = num2string[ss[c_id]]
    for i in range(0, len(tt)):
        path.append(tt[i])
        dfs(ss, num2string, c_id + 1, path, paths)
        path.pop()


def main(ss):
    num2string = {
        '2':'abc',
        '3':'def',
        '4':'ghi',
        '5':'jkl',
        '6':'mno',
        '7':'pqrs',
        '8':'tuv',
        '9':'wxyz',
    }

    path = []
    paths = []

    dfs(ss, num2string, 0, path, paths)
    return paths

if __name__ == '__main__':
    ss = '234'
    paths = main(ss)
   