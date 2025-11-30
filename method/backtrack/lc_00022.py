# coding=utf-8

def dfs(n, left_count, right_count, path, res):
    if len(path) == 2*n:
        res.append(''.join(path))
        return
    if left_count < n:
        path.append('(')
        dfs(n, left_count+1, right_count, path, res)
        path.pop()
    if right_count < left_count:
        path.append(')')
        dfs(n, left_count, right_count+1, path, res)
        path.pop()

def main(n):
    res = []
    path = []
    dfs(n, 0, 0, path, res)
    return res


if __name__ == '__main__':
    n = 2

    main(n)