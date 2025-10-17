# coding=utf-8


def main(array, target):
    l = 0
    r = len(array)-1

    while l < r:  # 有 r 存在直接替换 m 的情况，所以这里必须使用 < ，不然会出现死循环
        m = l + (r-l)//2
        if array[m] == target:
            r = m
        elif array[m] > target:
            r = m-1
        else:
            l = m+1
    if array[l] == target:
        return l
    else:
        return -1


if __name__ == '__main__':
    a = [1,1,1,2,2,6,7]
    target = 2
    print(main(a, target))
    