# coding=utf-8


def method_1(nums, target):
    if nums is None or len(nums)==0:
        return None
    visited = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in visited:
            return [visited[diff], i]
        visited[num] = i
    return None


if __name__ == '__main__':
    a =  [1,2,3,0,8]
    target = 11
    print(method_1(a, target))
