# coding=utf-8

def main(ss):
    # 计算每个字符最后一次的出现位置索引
    last_index = {c: i for i, c in enumerate(ss)}

    res = []
    max_index = -1
    l = 0  # 记录子串的起始
    r = 0
    while r < len(ss):
        c = ss[r]
        max_index = max(last_index[c], max_index)  # 从当前字符对应的索引和最大索引中取最大值
        if max_index == r:  # 如果当前索引等于最大值索引，说明找到了一个子串
            res.append(max_index-l+1)
            l = r+1  # 更新左指针
            max_index=-1  # 更新最大索引
        r+=1
    return res


if __name__ == '__main__':
    s = 'ababcbacadefegdehijhklij'
    res = main(s)
    print(res)
