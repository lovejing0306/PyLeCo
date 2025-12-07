# coding=utf-8

def search(ss, length):
    temp = set()
    for i in range(len(ss)-length+1):
        j = i + length
        sub = ss[i:j]
        if sub in temp:
            return sub
        temp.add(sub)
    return None

def main(ss):
    l = 0
    r = len(ss) - 1

    res = ''
    while l<=r:
        m = l + (r-l) // 2
        dup = search(ss, m)
        if dup is not None:
            res = dup
            l = m+1
        else:
            r = m-1
    return res


if __name__ == '__main__':
    # s = "banana"
    s = 'abcd'
    res = main(s)
    print(res)
