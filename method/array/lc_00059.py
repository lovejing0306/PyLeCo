# coding=utf-8

def main(matrix):
    r = 0
    l = len(matrix)-1
    i = 0
    j = 0
    res = []
    while i<=l and j <= l:
        while j <= l-1:  # 遍历顶部
            res.append(matrix[i][j])
            j+=1
        while i <= l-1:  # 遍历右部
            res.append(matrix[i][j])
            i+=1
        while j>=r+1:    # 遍历底部
            res.append(matrix[i][j])
            j-=1
        while i>=r+1:    # 遍历左部
            res.append(matrix[i][j])
            i-=1
        
        i+=1
        j+=1
        r+=1   # 缩减左边界
        l-=1   # 缩减右边界
    if len(matrix) % 2 == 1:
        res.append(matrix[len(matrix)//2][len(matrix)//2])

    return res


if __name__ == '__main__':
    matrix = [[1,2,3],[8,9,4],[7,6,5]]
    # matrix = [[1]]
    res = main(matrix)
    print(res)