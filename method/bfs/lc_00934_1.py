# coding=utf-8

def dfs(grid, m, n, i, j, dirs):
    if grid[i][j] == 0:
        return
    if grid[i][j] == 2:  # 如果已经等于 2 表示已经被访问过
        return

    grid[i][j] = 2
    
    for dir_ in dirs:
        x = i + dir_[0]
        y = j + dir_[1]
        if 0<=x < m and 0<=y<n:
            dfs(grid, m, n, x, y, dirs)

def main(grid):
    m = len(grid)
    n = len(grid[0])

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    flag = False
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                dfs(grid, m, n, i, j, dirs)
                flag = True
                break
        if flag:
            break
    
    queue = []
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                queue.append((i, j))
    flag = False
    count = 0
    while len(queue) > 0:
        new_queue = []
        for item in queue:
            i, j = item
            if grid[i][j] == 1:  # 如果当前位置的值为 1，说明已经找到了连接点，结束整个循环
                flag = True
                break
            for dir_ in dirs:
                x = i + dir_[0]
                y = j + dir_[1]
                # 如果坐标点合法，同时没有被访问过
                if 0<=x<m and 0<=y<n and grid[x][y] !=2:
                    if grid[x][y] == 0:
                        grid[x][y] = 2   # 将值为 0 的点设置为 2
                    new_queue.append((x, y))  # 将当前位置加入到新队列中
        if flag:
            break
        count += 1
        queue = new_queue
    return count-1


if __name__ == '__main__':
    # grid = [[0,1,0],[0,0,0],[0,0,1]]
    grid = [[0,1,0],[0,0,0],[0,0,1]]
    res = main(grid)
    print(res)