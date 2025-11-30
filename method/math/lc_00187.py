# coding=utf-8

def main(num, target):
    nums = list(range(num))

    del_num = 0
    cur_num = 0
    counter = 0
    while del_num < num-1:
        index = cur_num % num
        if nums[index] == -1:
            pass
        else:
            counter += 1
        if counter == target:
            nums[index] = -1
            del_num +=1
            counter = 0
        cur_num += 1
    
    for val in nums:
        if val == -1:
            continue
        return val
    return -1

if __name__ == '__main__':
    num = 12
    target = 5
    res = main(num, target)
    print(res)