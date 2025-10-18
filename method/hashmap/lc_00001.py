# coding=utf-8

def main(array, target):
    if array is None or len(array) == 0:
        return None
    
    dict_ = {}
    for i, value in enumerate(array):
        dict_[value] = i
        if (target - value) in dict_:
            return [dict_[target-value], i]
    return None


if __name__ == '__main__':
    a =  [1,2,3,0,8]
    target = 11
    print(main(a, target))
