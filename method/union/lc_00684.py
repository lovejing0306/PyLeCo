# coding=utf-8

def find(nums, n):
    # 找到下标索引和值相等的元素
    while n != nums[n]:
        n = nums[n]
    return n

def main(edges):
    nums = list(range(1001))
    for x, y in edges:
        p = find(nums, x)
        q = find(nums, y)
        if p == q:
            return [x, y]
        else:
            nums[p] = q
    return None


if __name__ == '__main__':
    edges = [[1,2], [1,3], [2,3]]
    res = main(edges)
    print(res)