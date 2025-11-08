# coding=utf-8

def main(matrix):
    matrix.sort(key=lambda x : (-x[0], x[1]))  # 对第一个维度进行倒排，第二个维度执行正排
    
    mm = []
    for i in range(len(matrix)):
        m = matrix[i]
        mm.insert(m[1], m)  # 它的第二个维度就是插入的位置
    return mm


if __name__ == '__main__':
    mm = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
    res = main(mm)
    print(res)