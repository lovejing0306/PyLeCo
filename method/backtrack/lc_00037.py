# coding=utf-8

def is_valid(n, matrix, row, col, value):
    for i in range(n):
        if matrix[row][i] == value:
            return False
    
    for i in range(n):
        if matrix[i][col] == value:
            return False
    
    row_id = row // 3 * 3
    col_id = col // 3 * 3

    for r in range(row_id, row_id + 3):
        for c in range(col_id, col_id + 3):
            if matrix[r][c] == value:
                return False
    return True


def dfs(n, ss, matrix):
    for r in range(0, n):    # 每次都从 0 开始
        for c in range(0, n):  # 每次都从 0 开始
            if matrix[r][c] != '.': 
                continue
            for i in range(len(ss)):
                if is_valid(n, matrix, r, c, ss[i]) is False:
                    continue
                matrix[r][c] = ss[i]
                flag = dfs(n, ss, matrix)
                if flag:
                    return True
                matrix[r][c] = '.'
            return False
    return True

def main(board, n):
    """ 
    这种解法会超时
    """
    ss = "123456789"
    dfs(n, ss, board)


if __name__ == '__main__':
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    main(board, 9)
    print(board)