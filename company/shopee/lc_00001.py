# coding=utf-8

def main(nums, k):
    """
    找出整型数组中和为 k 的二元组，数组中包含重复元素
    """
    if nums is None or len(nums) == 0:
        return []
    
    res = set()  # 存放符合条件的二元组
    visited = set()  # 存放访问过的元素

    for num in nums:
        sub = k - num
        if sub in visited:
            # 将较小的值放在前面，较大的值放到后面
            if sub < num:
                res.add((sub, num))
            else:
                res.add((num, sub))
        else:
            visited.add(num)

    return list(res)

if __name__ == '__main__':
    nums = [1,5,7,-1,5]
    k = 6
    res = main(nums, k)
    print(res)
