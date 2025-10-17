# coding=utf-8

def main(array, target):
    l = 0
    r = len(array)-1

    while l <= r:
        m = l + (r-l)//2   # 一定要使用这种方式计算中间索引
        if array[m] == target:
            return m
        elif array[m] > target:
            r = m-1
        else:
            l = m+1
    return -1


if __name__ == '__main__':
    a = [1,2,3,4,7,9]
    target = 7
    print(main(a, target))
