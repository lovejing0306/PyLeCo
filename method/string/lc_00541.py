# coding=utf-8

def main(s, k):
    if k <=1:
        return s

    l = 0
    r = 0
    res = []
    while r < len(s):
        if r-l+1 == 2 * k:
            res.append(s[l:l+k][::-1])
            res.append(s[l+k:r+1])
            r+=1
            l = r
        else:
            r +=1
    
    if k <= r-l:
        res.append(s[l:l+k][::-1])
        res.append(s[l+k:r])
    elif 0< r-l:
        res.append(s[l:r][::-1])
    res = ''.join(res)
    return res


if __name__ == '__main__':
    s = "abcd"
    k = 2
    res = main(s, k)
    print(res)