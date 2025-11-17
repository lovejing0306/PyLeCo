# coding=utf=8

def get_five_num(n):
    count = 0
    while n!=0:
        a = n // 5
        b = n % 5
        if b != 0 :
            break
        n = a
        count += 1
    return count


def main(num):
    """ 
    统计能够被 5 整除的数字中 5 的个数
    """
    count = 0
    for i in range(1, num+1):
        count += get_five_num(i)
    return count


if __name__ == '__main__':
    n = 5
    res = main(15)
    print(res)