# coding=utf-8
import sys

def main(nums):
    """ 
    给定由 n 个正整数组成的数组，将它拆分多个严格递减子序列，输出通过拆分可以获得的最少子序列个数，并输出这些子序列。
    贪心
    """
    
    seqs = []
    for num in nums:
        target_index = -1
        min_val = sys.maxsize

        for i, seq in enumerate(seqs):
            # 找到 尾元素最小的序列，同时满足 当前值 num 小于该尾元素
            if seq[-1] > num and seq[-1] < min_val:
                target_index = i
                min_val = seq[-1]
        
        if target_index != -1:
            seqs[target_index].append(num)
        else: # 如果在已经存在的序列中没有找到符合要求的序列，则创建新的序列
            seqs.append([num])
    return seqs


if __name__ == '__main__':
    nums = [5,3,4,2,1]
    print(main(nums))
