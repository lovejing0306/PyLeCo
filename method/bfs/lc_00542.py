# coding=utf-8
import queue

def bfs(matrix):
    if matrix is None:
        return matrix
    
    dirs = [(0,1), (0,-1), (-1,0), (1, 0)]

    res = []
    for _ in range(len(matrix)):
        res.append([0] * len(matrix[0]))
    
    visited = []
    for _ in range(len(matrix)):
        visited.append([False] * len(matrix[0]))
    
    qq = queue.Queue()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                qq.put((i, j))
                visited[i][j] = True
    
    count = 0
    while qq.qsize() > 0:
        for _ in range(qq.qsize()):  # 访问同一层的所有元素
            i, j = qq.get()

            if matrix[i][j] == 1:
                res[i][j] = count
            for dir in dirs:
                x = i + dir[0]
                y = j + dir[1]
                if x >=0 and y >=0 and x < len(matrix[0]) and y < len(matrix) and visited[x][y] is False:
                    qq.put((x, y))
                    visited[i][j] = True
                    
        count += 1
    return res


if __name__ == '__main__':
    mat = [[0,0,0],[0,1,0],[1,1,1]]
    res = bfs(mat)
    print(res)