# coding=utf-8

from re import M


def main(array, target):
    if array is None:
        return -1
    
    if target <= array[0]:
        return 0
    
    if target >= array[-1]:
        return len(array)-1
    
    l = 0 
    r = len(array)-1
    
    # 完全使用了 基本二分查找的思路，如果最终没有找到 target，则只需要判断 target 举例 左右指针哪个值更近
    while l <= r:  # 由于最后需要使 r 在 l 的左边，所以需要使用 <=
        m = l + (r-l)//2

        if array[m] == target:
            return m
        elif array[m] > target:
            r = m-1
        else:
            l = m+1
    
    return r if abs(target - array[r]) <= abs(target-array[l]) else l


if __name__ == '__main__':
    a = [1,4]
    target = 2
    print(main(a, target))