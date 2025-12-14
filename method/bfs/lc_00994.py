# coding=utf-8

def main(grid):
    m = len(grid)
    n = len(grid[0])

    good = 0
    queue = []
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                queue.append((i, j))
            if grid[i][j] == 1:
                good+=1
    if good == 0:
        return 0
    
    dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    count = 0

    bad = 0
    while len(queue) > 0:
        new_queue = []
        for item in queue:
            for dir_ in dirs:
                x = item[0] + dir_[0]
                y = item[1] + dir_[1]
                if 0<= x < m and 0 <=y < n:
                    if grid[x][y] == 0:
                        continue
                    if grid[x][y] == 2:
                        continue
                    grid[x][y] = 2  # 将好橘子标记为 腐烂
                    bad += 1
                    new_queue.append((x, y))
        count += 1
        queue = new_queue
    return count-1 if bad == good else -1


if __name__ == '__main__':
    grid = [[0,2]]
    res = main(grid)
    print(res)