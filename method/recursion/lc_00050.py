# coding=utf-8

def main(x, n):
    if n==0:
        return 1
    if n==1:
        return x
    res = main(x, n//2)
    res *= res
    if n%2 == 1:
        res *= x
    return res

if __name__ == '__main__':
    x = 2
    n = 7
    print(main(x, n))
