# coding=utf-8

def build_prefix(s):
    prefix = [0] * len(s)

    j = 0
    for i in range(1, len(s)):  # 这里需要从位置 1 开始，因为位置 0 没有有效的前缀和后缀
        while j>0 and s[i] != s[j]:  # j 必须满足 j>0
            j = prefix[j-1]
        if s[i] == s[j]:
            j+=1  # 如果两个位置的字符相同，则 j 自增 1
        prefix[i] = j  # 记录在每个位置 i 时，前缀和后缀中匹配字符的最长长度
    return prefix

if __name__ == '__main__':
    # ss = 'banana'
    ss = 'ananab'
    nums = build_prefix(ss)
    print(nums)
