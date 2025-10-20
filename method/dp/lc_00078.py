# coding=utf-8
import copy

def main(nums):
    # 状态：数组中前 n 个元素，组成的排列组合形式
    # 初始化：数组中的没有元素是，加入空集合
    dp = [[]]

    # 遍历每个新增的元素
    for i, num in enumerate(nums):
        # 访问前 i-1 个数组成的排列组合
        for j in range(len(dp)):
            a = copy.deepcopy(dp[j])  # 拷贝一份
            a.append(num)  # 在排列组合的后面添加当前元素
            dp.append(a)
    return dp


if __name__ == '__main__':
    nums = [1,3,4,7]
    res = main(nums)

    print(res)
    print(len(res))
