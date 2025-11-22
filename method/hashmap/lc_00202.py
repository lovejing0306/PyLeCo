# coding=utf-8

def main(n):
    """ 
    关键点在于，“也可能是 无限循环 但始终变不到 1。”
    """
    visited = set()
    while n!=1:
        sum_ = 0
        while n!=0:
            a = n//10
            b = n%10
            sum_ += b**2
            n = a
        if sum_ in visited:
            return False  # 出现了重复，说明有循环了
        else:
            visited.add(sum_)
        n = sum_
    return True


if __name__ == '__main__':
    n = 2
    print(main(n))