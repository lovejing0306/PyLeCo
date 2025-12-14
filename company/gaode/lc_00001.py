# coding=utf-8

def main(n):
    """ 
    求一个实数的立方根，误差控制在 1e-5
    思路：
    二分查找
    1. 确定搜索区间：
        * 对于正数 n，立方根在 [0, n] 范围内（当 n ≥ 1）或 [0, 1] 范围内（当 0 < n < 1）
        * 对于负数 n，立方根在 [n, 0] 范围内
    2. 二分查找：
        * 取中点 mid，计算 mid^3
        * 如果 mid^3 与目标值的差距小于 1e-5，则找到答案
        * 如果 mid^3 < n，说明立方根在右半部分
        * 如果 mid^3 > n，说明立方根在左半部分
    3. 循环终止条件：当搜索区间足够小（右边界 - 左边界 < 1e-5）或找到满足精度的解时停止
    """
    if n==0:
        return 0.
    if n > 0:
        if n >= 1:
            left, right = 0, n
        else:
            left, right = 0, 1
    else:
        if n <= -1:
            left, right = n, 0
        else:
            left, right = -1, 0
    
    while right - left > 1e-6:
        m = left + (right - left) / 2
        tt = m * m * m

        if abs(tt-n) < 1e-5:
            return m
        if tt < n:
            left = m
        else:
            right = m
    return left + (right - left) / 2


if __name__ == '__main__':
    n = 0.125
    res = main(n)
    print(res)
