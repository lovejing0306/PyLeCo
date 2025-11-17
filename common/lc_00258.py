# coding=utf-8

def temp(num):
    sum_ = 0
    n  = num
    while n !=0:
        a = n // 10
        b = n % 10
        sum_ += b
        n = a
    return sum_


def method_1(num):
    while num >= 10:
        num = temp(num)
    return num


def method_2(num):
    if num < 10:
        return num
    
    b = num % 9
    # 如果除以 9 的余数为 0，则返回 9，否则，返回余数
    return 9 if b==0 else b


if __name__ == '__main__':
    for i in range(1, 40):
        res = method_1(num=i)
        print(i, res)
