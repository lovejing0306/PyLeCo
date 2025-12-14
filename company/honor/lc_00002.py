# coding=utf-8

def dfs(point, visited, valid_points, path):
    if point not in valid_points:
        return
    if point in visited:
        return 
    path.append(point)
    visited[point] = True
    i, j = point
    for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
        dfs((x, y), visited, valid_points, path)
    

def main(matrix, nums):
    """ 
    一个固定的5x5矩阵,判断给出的6个数字是否都相邻在一起，上下左右就是相邻
    本质上是判断给定的 6 个点是否在一个连通区域内
    """

    nums = set(nums)
    valid_points = []
    # 找出 6 个点的位置
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] in nums:
                valid_points.append((i, j))

    path = []
    point = valid_points[0]
    valid_points = set(valid_points)
    visited = {}
    # 判断从其中一个点是否能够到达其它任意点
    dfs(point, visited, valid_points, path)
    return True if len(path) == 6 else False


if __name__ == '__main__':
    matrix = [
        [1,2,3,4,5],
        [11,12,63,14,15],
        [41,22,43,26,25],
        [31,52,30,34,65],
        [41,42,93,45,75]
    ]
    nums = [1,2,3,4,5,11]
    # nums = [1,2,11,14,25,15]

    res = main(matrix, nums)
    print(res)