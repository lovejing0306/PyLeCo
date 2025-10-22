# coding=utf-8
import copy


def is_palindrome(s, i, j):
    while i<=j:
        if s[i] == s[j]:
            i+=1
            j-=1
        else:
            return False
    return True


def dfs(s, start_id, path, paths):
    if len(s) == start_id:
        paths.append(copy.deepcopy(path))
        return
    
    for i in range(start_id, len(s)):
        if is_palindrome(s, start_id, i): # 当找到一个回文串时，加入到路径中，然后从剩余的子串中接着查找
            path.append(s[start_id:i+1])
        else: # 如果没有找到回文串，则一致找
            continue
        dfs(s, i+1, path, paths)
        path.pop()


def main(s):
    paths = []
    path = []
    dfs(s, 0, path, paths)
    return paths


if __name__ == '__main__':
    s = 'aab'
    paths = main(s)
    print(paths)


