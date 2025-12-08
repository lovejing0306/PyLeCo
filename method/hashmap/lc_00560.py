# coding=utf-8

def main(nums, k):
    sum_ = 0
    mapping = {0:1}   # 需要将和为 0 初始化为出现 1 次
    res = 0
    for num in nums:
        sum_ += num
        diff = sum_ - k
        if diff in mapping:  # 查看 mapping 是否出现过和为 diff 的子序列
            res += mapping[diff]
        # 记录在每个位置上的 sum_
        mapping[sum_] = mapping.get(sum_, 0) + 1
    return res


if __name__ == '__main__':
    a = [1,2,3]
    k = 0

    print(main(a, k))
