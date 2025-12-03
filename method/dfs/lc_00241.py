# coding=utf-8

def dfs(items, start_index, end_index):
    # 如果起始索引大于等于结束索引，则返回
    if start_index >= end_index:
        return [items[start_index]]  # 返回单个元素的集合
    
    res = []  # 记录左右两边的运算结果
    for i in range(start_index, end_index+1):
        if items[i] not in ['+', '-', '*']:  # 如果不是运算符，则直接跳过
            continue
        res_l = dfs(items, start_index, i-1)  # 求左边的计算结果，返回的是结果集合
        res_r = dfs(items, i+1, end_index)    # 求右边的计算结果
        # 对左右两边的结果集合，求计算结果
        for a in res_l:
            for b in res_r:
                if items[i] == '+':
                    c = a+b
                elif items[i] == '-':
                    c = a-b
                elif items[i] == '*':
                    c = a*b
                res.append(c)
    return res  # 返回运算结果


def main(ss):
    items = []
    # 将字符串拆分成单一元素，主要是对大数的拆分，如：33，566
    i = 0
    while i < len(ss):
        c = ss[i]
        if c in ['+', '-', '*']:
            items.append(c)
            i+=1
        else:
            j = i
            while j < len(ss) and ss[j] not in ['+', '-', '*']:
                j+=1
            num = int(ss[i:j])
            items.append(num)
            i=j
    
    res = dfs(items, 0, len(items)-1)
    return res

if __name__ == '__main__':
    s = '2-1-1'
    main(s)