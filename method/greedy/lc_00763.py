# coding=utf-8

def main(ss):
    ss_dict = {}

    for i in range(len(ss)):
        ss_dict[ss[i]] = i
    
    start = 0
    end = 0   # 记录最远的索引
    res = []   # 存放子序列的长度
    
    for i in range(len(ss)):
        end = max(end, ss_dict[ss[i]])
        if i == end:
            res.append(end-start+1)
            start = end + 1
    return res


if __name__ == '__main__':
    s = "eccbbbbdec"
    s = "ababcbacadefegdehijhklij"
    res = main(s)
    print(res)