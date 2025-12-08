# coding=utf-8


def main(nums, target):
    mapping = {}  # 使用 哈希表 记录访问过的元素和对应的索引
    
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in mapping:
            return [mapping[diff], i]
        else:
            mapping[nums[i]] = i
    return [-1, -1]


if __name__ == '__main__':
    a =  [1,2,3,0,8]
    target = 11
    print(main(a, target))
