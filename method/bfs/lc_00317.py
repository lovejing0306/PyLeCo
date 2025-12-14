# coding=utf-8

def get_dist(grid, point, ones, dirs):
    m = len(grid)
    n = len(grid[0])

    queue = [point]
    visited = {point}
    visited_ones = set()

    dist = 0
    step = 1
    counter = 0
    flag = False

    while len(queue) > 0:
        new_queue = []
        for item in queue:
            for dir_ in dirs:
                x = item[0] + dir_[0]
                y = item[1] + dir_[1]
                if 0<= x < m and 0 <= y < n:
                    if grid[x][y] == 2:
                        continue
                    if grid[x][y] == 1 and (x, y) not in visited_ones:
                        counter += 1
                        dist += step
                        visited_ones.add((x, y))
                    if counter == ones:
                        flag = True
                        break
                    if grid[x][y] == 0 and (x, y) not in visited:
                        new_queue.append((x, y))
                        visited.add((x, y))
            if flag:
                break
        if flag:
            break
        step += 1
        queue = new_queue
    return dist if flag else  -1


def method_1(grid):
    """ 
    问题描述：
    你是个房地产开发商，想要选择一片空地建一栋大楼。你想把这栋大楼够造在一个距离周边设施都比较方便的地方。通过调研，你希望从它出发能在最短的距离和内抵达周边全部的建筑物。请你计算出这个最佳的选址到周边全部建筑物的最短距离和。
    提示：
    你只能通过向上、下、左、右四个方向上移动。
    给你一个由 0、1 和 2 组成的二维网格，其中：

    0 代表你可以自由通过和选择建造的空地
    1 代表你无法通行的建筑物
    2 代表你无法通行的障碍物

    示例：
    输入：[[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
    1 - 0 - 2 - 0 - 1
    |   |   |   |   |
    0 - 0 - 0 - 0 - 0
    |   |   |   |   |
    0 - 0 - 1 - 0 - 0

    输出：7

    解析：
    给定三个建筑物 (0,0)、(0,4) 和 (2,2) 以及一个位于 (0,2) 的障碍物。
    由于总距离之和 3+3+1=7 最优，所以位置 (1,2) 是符合要求的最优地点，故返回7。

    注意：
    题目数据保证至少存在一栋建筑物，如果无法按照上述规则返回建房地点，则请你返回 -1。
    """
    ones = 0
    m = len(grid)
    n = len(grid[0])

    zeros = []
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                ones += 1
            if grid[i][j] == 0:
                zeros.append((i, j))

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    min_val = float('inf')
    for point in zeros:
        res = get_dist(grid, point, ones, dirs)
        if res == -1:
            continue
        min_val = min(res, min_val)
    return min_val if min_val < float('inf') else -1


if __name__ == '__main__':
    grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
    res = method_1(grid)
    print(res)