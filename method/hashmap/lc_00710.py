import random  # 使用内置随机库

class Solution:

    def __init__(self, n, blacklist):
        m = len(blacklist)  # 黑名单的数量
        self.bound = n - m  # 压缩后的等概率取样区间长度；最终允许的整数总数
        self.map = dict()   # 映射表：将压缩区间内的“黑名单数”映射到尾部区间的“合法数”
        i = self.bound      # 尾部候选指针，起始为 bound，向右寻找未被黑名单占用的合法数
        bset = set(blacklist)  # 将黑名单转为集合，便于 O(1) 判断与去重
        for black in blacklist:  # 遍历每个黑名单数
            if black < self.bound:  # 只处理压缩区间 [0, bound-1] 中的黑名单数
                while i in bset:     # 若尾部候选位置 i 也在黑名单，则跳过，继续右移
                    i += 1
                self.map[black] = i  # 将该黑名单数映射到当前尾部的一个合法位置 i
                i += 1               # 尾部候选指针右移，供下一个映射使用

    def pick(self) -> int:
        # 在 [0, bound-1] 上等概率随机一个数 r；
        # 若 r 是“压缩区间里的黑名单”，则通过映射得到一个尾部合法数，否则直接返回 r
        r = random.randint(0, self.bound - 1)
        return self.map.get(r, r)

    
def main(n, black_list):
    m = len(black_list)  # 黑名单的数量
    bound = n - m  # 压缩后的等概率取样区间长度；最终允许的整数总数
    mapping = {}   # 映射表：将压缩区间内的“黑名单数”映射到尾部区间的“合法数”

    i = bound     # 尾部候选指针，起始为 bound，向右寻找未被黑名单占用的合法数
    bset = set(black_list)   # 将黑名单转为集合，便于 O(1) 判断与去重
    for black in black_list:  # 遍历每个黑名单数
        if black < bound:  # 只处理压缩区间 [0, bound-1] 中的黑名单数
            while i in bset:     # 若尾部候选位置 i 也在黑名单，则跳过，继续右移
                i += 1
            mapping[black] = i  # 将该黑名单数映射到当前尾部的一个合法位置 i
            i += 1     
    
    r = random.randint(0, bound - 1)
    res = mapping.get(r, r)
    return res


if __name__ == '__main__':
    res = main(5, [2])
    print(res)
