# coding=utf-8

def main(s):
    if s is None or len(s) == 0:
        return s
    
    l = 0
    r = len(s)-1

    while l < r:
        t = s[l]
        s[l] = s[r]
        s[r] = t
        l+=1
        r-=1
    return s


if __name__ == '__main__':
    s = ["H","a","n","n","a","h"]
    res = main(s)
    print(res)
