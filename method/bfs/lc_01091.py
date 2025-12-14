# coding=utf-8

def main(grid):
    m = len(grid)
    n = len(grid[0])

    if grid[0][0] != 0:
        return -1
    if grid[-1][-1] != 0:
        return -1

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, 1), (1, -1)]

    queue = [(0, 0)]
    visited = {(0, 0)}
    count = 0
    flag = False

    while len(queue) > 0:
        new_queue = []
        for item in queue:
            if item[0] == m-1 and item[1] == n-1:
                flag = True
                break
            for dir_ in dirs:
                x = item[0] + dir_[0]
                y = item[1] + dir_[1]
                if 0 <= x <m and 0<=y < n:
                    if grid[x][y] == 1:
                        continue
                    if (x, y) in visited:
                        continue
                    new_queue.append((x, y))
                    visited.add((x, y))
        count += 1
        if flag:
            break
        queue = new_queue
    return count if flag else -1


if __name__ == '__main__':
    grid = [[1,0,0],[1,1,0],[1,1,0]]
    res = main(grid)
    print(res)