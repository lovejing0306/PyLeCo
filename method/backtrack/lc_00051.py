# coding=utf-8


def is_valid(n, matrix, r_id, c_id):
    r_id_1 = r_id
    c_id_1 = c_id
    while r_id_1 >= 0 and c_id_1 >= 0:
        if matrix[r_id_1][c_id_1] == 'Q':
            return False
        r_id_1 -= 1
        c_id_1 -= 1
    
    r_id_2 = r_id
    c_id_2 = c_id
    while r_id_2 >=0 and c_id_2 < n:
        if matrix[r_id_2][c_id_2] == 'Q':
            return False
        r_id_2 -=1
        c_id_2 +=1

    return True

def dfs(n, layer_id, visited, matrix, paths):
    if layer_id == n:  # 如果访问到的层数和总层数相同，则记录结果
        path = []
        for item in matrix:
            path.append(''.join(item))
        paths.append(path)
        return 
    
    for i in range(n):
        if visited[i]:  # 判断同一列是否有冲突
            continue
        flag = is_valid(n, matrix, layer_id, i)  # 判断两个对角线是否有冲突
        
        if flag is False:
            continue
        matrix[layer_id][i] = 'Q'
        visited[i] = True
        dfs(n, layer_id + 1, visited, matrix, paths)
        visited[i] = False
        matrix[layer_id][i] = '.'


def main(n):
    paths = []
    visited = {}
    matrix = []
    for i in range(n):
        visited[i] = False
    for i in range(n):
        matrix.append(['.']*n)
    
    dfs(n, 0, visited, matrix, paths)
    return paths


if __name__ == '__main__':
    paths = main(5)
    print(paths)
