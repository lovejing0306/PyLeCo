# coding=utf-8

def dfs(grid, m, n, directory, i, j, queue):
    """
    使用深度优先遍历将其中一座岛标记为 2
    """
    if i < 0 or i >=m:
        return
    if j < 0 or j >=n:
        return
    if grid[i][j] == 2:  # 如果等于 2 表示已经访问过该点
        return
    if grid[i][j] == 0:  # 如果等于 0 不是陆地
        return
    
    grid[i][j] = 2  # 将坐标点标记为 2
    queue.append((i, j))  # 记录岛屿的坐标点，用于执行广度优先搜索
    for item in directory: # 分别遍历 4 个方向
        i_ = i + item[0]
        j_ = j + item[1]
        dfs(grid, m, n, directory, i_, j_, queue)


def main(grid):
    m = len(grid)
    n = len(grid[0])

    directory = [
        [1, 0], [-1, 0], [0, -1], [0, 1]
    ]  # 枚举四个方向
    queue = []
    flag = False
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:  # 如果找一个标记为 1 的点，则立即执行符号替换
                dfs(grid, m, n, directory, i, j, queue)
                flag = True
                break
        if flag:
            break
    
    step = 0  # 记录需要走的步数
    flag = False
    while len(queue) > 0:
        new_queue = []  # 创建新的队列，记录下一次可访问的点
        for point in queue:  # 访问当前队列
            for item in directory:  # 访问四个方向
                i = point[0] + item[0]
                j = point[1] + item[1]
                if i < 0 or i >=m:  # 如果超出边界，则跳过
                    continue
                if j < 0 or j >=n:
                    continue
                if grid[i][j] == 2:  # 如果已经被标记为 2，则跳过
                    continue
                if grid[i][j] == 0:  # 如果是 0 ，则被标记为 2
                    grid[i][j] = 2
                    new_queue.append((i, j))
                if grid[i][j] == 1:  # 如果是 1，说明已经找到了另一个岛屿
                    flag = True
                    break
            if flag:
                break
        if flag:
            break
        step += 1
        queue = new_queue  # 下一次可访问的队列元素

    return step


if __name__ == '__main__':
    # grid = [
    #     [1,1,1,1,1],
    #     [1,0,0,0,1],
    #     [1,0,1,0,1],
    #     [1,0,0,0,1],
    #     [1,1,1,1,1]
    # ]
    grid = [
        [0,1],[1,0]
    ]

    res = main(grid)
    print(res)