# coding=utf-8

def main(ss, numRows):
    if numRows == 1:
        return ss
    if numRows == 2:
        s1 = ss[0::2]
        s2 = ss[1::2]
        return s1 + s2
    
    res = []
    step = 2 * numRows - 2
    for i in range(numRows):
        if i == 0 or i == numRows-1: # 第一行和最后一行为单一步长
            j = i
            while j < len(ss):
                res.append(ss[j])
                j+=step
        else:   # 中间行为 双步长
            l = i
            r = -i + step  # -i 为小技巧
            while l < len(ss) and r < len(ss):
                res.append(ss[l])
                res.append(ss[r])
                l += step
                r += step
            if l < len(ss):
                res.append(ss[l])
    res = ''.join(res)
    return res


if __name__ == '__main__':
    s = 'LEETCODEISHIRING'
    n = 4
    res = main(s, n)
    print(res)