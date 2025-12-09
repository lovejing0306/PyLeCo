# coding=utf-8

def dfs(x, n):
    if n == 0:
        return 1
    if n % 2 == 1:
        y = dfs(x, n//2)
        y = y * y * x
    else:
        y = dfs(x, n//2)
        y = y * y
    return y


def main(x, n):
    if n < 0:
        return 1. / dfs(x, abs(n))
    else:
        return dfs(x, n)


if __name__ == '__main__':
    x = 2.0
    n = -2
    res = main(x, n)
    print(res)