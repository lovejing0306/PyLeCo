# coding=utf-8

def main(array, target):
    l = 0
    r = len(array) -1 

    while l < r:
        m = l + (r-l)//2
        if array[m] == target:
            l = m
        elif array[m] > target:
            r = m-1
        else:
            l = m+1
    
    return -1 if array[l] != target else l


if __name__ == '__main__':
    a = [1,1,1,2,2,6,7]
    target = 2
    print(main(a, target))