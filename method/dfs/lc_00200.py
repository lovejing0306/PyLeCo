# coding=utf-8

def dfs(grid, i, j, visited, dirs):
    if grid[i][j] == '0':
        return
    
    for dir in dirs:
        y = i + dir[0]
        x = j + dir[1]
        
        if 0<= x < len(grid[0]) and 0<= y < len(grid) and visited[y][x] is False:
            visited[y][x] = True
            dfs(grid, y, x, visited, dirs)


def main(grid):
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    visited = []
    for _ in range(len(grid)):
        visited.append([False] * len(grid[0]))
    
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1" and visited[i][j] is False:
                count += 1
                visited[i][j] = True
                dfs(grid, i, j, visited, dirs)
    return count


if __name__ == '__main__':
    grid = [
        ['1','1','0','0','0'],
        ['1','1','0','0','0'],
        ['0','0','1','0','0'],
        ['0','0','0','1','1']
    ]
    count = main(grid)
    print(count)
