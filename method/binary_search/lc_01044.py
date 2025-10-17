# coding=utf-8

def is_find(s, l):
    """
    01234
    """
    container = set()
    i = 0
    while i <= len(s)-l:
        sub = s[i:i+l]  # 实际取值是最后索引的前一位
        if sub in container:
            return sub
        else:
            container.add(sub)
        i += 1
    return ''

def main(s):
    res = ''
    if s is None or len(s)==0:
        return res

    l = 0
    r = len(s)-1
    while l < r:
        m = l + (r-l + 1)//2  # 这里很关键
        res = is_find(s, m)
        if res !='':
            l = m
        else:
            r = m-1
    
    res_ = is_find(s, l)
    if res_ != '':
        return res_
    else:
        res


if __name__ == '__main__':
    s = 'aaaaa'
    print(main(s))
