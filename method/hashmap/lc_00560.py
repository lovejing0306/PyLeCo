# coding=utf-8

def main(array, k):
    count = 0
    if array is None or len(array) == 0:
        return count

    s = 0
    hash_map = {0:1}
    
    for value in array:
        s += value
        # 必须在同一个循环中完成“差值是否存在”和“记录元素和”的操作
        # 不能先记录元素的和，再判断差值出现的次数
        if s - k in hash_map:
            count += hash_map[s - k]
        hash_map[s] = 1 if s not in hash_map else hash_map[s] + 1
    return count


if __name__ == '__main__':
    a = [1,2,3]
    k = 0

    print(main(a, k))
