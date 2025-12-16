# coding=utf-8

def dfs(grid, m, n, i, j, dirs):
    if grid[i][j] == '0':
        return

    grid[i][j] = '0'
    for dir_ in dirs:
        x = i + dir_[0]
        y = j + dir_[1]
        if 0 <= x < m and 0 <= y <n:
            dfs(grid, m, n, x, y, dirs)


def main(grid):
    m = len(grid)
    n = len(grid[0])
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                dfs(grid, m, n, i, j, dirs)
                count += 1
    return count


if __name__ == '__main__':
    # grid = [
    #     ['1','1','1','1','0'],
    #     ['1','1','0','1','0'],
    #     ['1','1','0','0','0'],
    #     ['0','0','0','0','0']
    # ]
    grid = [
        ['1','1','0','0','0'],
        ['1','1','0','0','0'],
        ['0','0','1','0','0'],
        ['0','0','0','1','1']
    ]
    res = main(grid)
    print(res)
