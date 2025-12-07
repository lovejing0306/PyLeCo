# coding=utf-8

def candidates(i, j, rows, cols, boxes, ss="123456789"):
    b = (i//3)*3 + (j//3)
    used = rows[i] | cols[j] | boxes[b]
    return [c for c in ss if c not in used]


def dfs(board, k, points, rows, cols, boxes, ss="123456789"):
    if k == len(points):
        return True
    best = k
    best_cands = None
    for idx in range(k, len(points)):
        x, y = points[idx]
        cands = candidates(x, y, rows, cols, boxes, ss)
        if best_cands is None or len(cands) < len(best_cands):
            best = idx
            best_cands = cands
            if len(best_cands) == 0:
                break
    if best_cands is None or len(best_cands) == 0:
        return False
    if best != k:
        points[k], points[best] = points[best], points[k]
    x, y = points[k]
    b = (x//3)*3 + (y//3)
    for c in best_cands:
        board[x][y] = c
        rows[x].add(c)
        cols[y].add(c)
        boxes[b].add(c)
        if dfs(board, k+1, points, rows, cols, boxes, ss):
            return True
        rows[x].remove(c)
        cols[y].remove(c)
        boxes[b].remove(c)
        board[x][y] = '.'
    return False


def main(board):
    """ 
    需要使用 哈希表 来判断是否有重复
    """
    m = len(board)
    n = len(board[0])

    rows = [set() for _ in range(m)]
    cols = [set() for _ in range(n)]
    boxes = [set() for _ in range((m//3)*(n//3))]

    points = []
    for i in range(m):
        for j in range(n):
            c = board[i][j]
            if c == '.':
                points.append((i, j))
            else:
                rows[i].add(c)
                cols[j].add(c)
                boxes[(i//3)*3 + (j//3)].add(c)
    dfs(board, 0, points, rows, cols, boxes)


if __name__ == '__main__':
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    main(board=board)
    print(board)
