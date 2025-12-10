# coding=utf-8

def method_1(grid):
    """ 
    这种解法会超时
    """
    
    m = len(grid)
    n = len(grid[0])

    dire = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    matrix = []
    for _ in range(m):
        matrix.append([0] * n)

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                continue

            visited = {(i, j)}
            queue = [(i, j)]
            count = 0
            flag = False

            while len(queue) > 0:
                new_queue = []
                for k in range(len(queue)):
                    x, y = queue[k]
                    if grid[x][y] == 0:
                        flag = True
                        break
                    for item in dire:
                        x_ = x + item[0]
                        y_ = y + item[1]
                        if 0<=x_ < m and 0 <= y_ < n and (x_, y_) not in visited:
                            new_queue.append((x_, y_))
                            visited.add((x_, y_))
                if flag:
                    break
                count += 1
                queue = new_queue
            matrix[i][j] = count

    return matrix


def method_2(grid):
    """ 
    计算从 0 到 1 的距离
    """
    m = len(grid)
    n = len(grid[0])

    queue = []  # 记录当前可访问的位置
    visited = set()  # 记录已经访问过的位置
    # 遍历矩阵，将值为 0 的位置放入到队列中，同时标记为已经被访问的状态
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                queue.append((i, j))
                visited.add((i, j))
    # 遍历方向
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    count = 0
    while len(queue) > 0:
        new_queue = [] # 创建新的队列，记录新的可以被访问的位置
        for point in queue:  # 访问当前队列中每个合法位置
            x, y = point
            if grid[x][y] == 1:  # 如果位置的值为 1，则修改路径长度
                grid[x][y] = count
            
            for item in dirs:  # 遍历每个方向
                x_ = x+item[0]
                y_ = y+item[1]
                # 如果新的位置合法，并且没有被访问过
                if 0<=x_ < m and 0<=y_ < n and (x_, y_) not in visited:
                    new_queue.append((x_, y_))
                    visited.add((x_, y_))
        count += 1  # 更新层的数量
        queue = new_queue  # 更新队列
    return grid


if __name__ == '__main__':
    mat = [[0,0,0],[0,1,0],[1,1,1]]
    res = method_2(mat)
    print(res)
