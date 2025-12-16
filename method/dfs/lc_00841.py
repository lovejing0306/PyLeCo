# coding=utf-8

def dfs(rooms, idx, visited):
    visited.add(idx)
    for index in rooms[idx]:
        if index in visited:
            continue
        dfs(rooms, index, visited)

def main(rooms):
    visited = set()
    dfs(rooms, 0, visited)
    return True if len(visited) == len(rooms) else False

if __name__ == '__main__':
    # rooms = [[1],[2],[3],[]]
    rooms = [[1,3],[3,0,1],[2],[0]]
    res = main(rooms)
    print(res)