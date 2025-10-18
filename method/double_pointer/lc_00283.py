# coding=utf-8

def main(array):
    if array is None or len(array) == 0:
        return array
    
    i = len(array)-1
    j = len(array)-1

    while j >=0:
        if array[j] == 0:
            array[i], array[j] = array[j], array[i]
            i -= 1
            j -= 1
        else:
            j -=1
    # python3 中的 list 是可变类型，可直接修改  


if __name__ == '__main__':
    a = [1,2,0,3,0,8]
    main(a)
    print(a)
    