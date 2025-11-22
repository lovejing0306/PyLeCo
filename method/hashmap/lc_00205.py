# coding=utf-8

def main(s, t):
    """ 
    重点在于结构必须保持一致
    """
    if s is None or t is None:
        return False
    if len(s) != len(t):
        return False
    if len(s) == 0 or len(t) == 0:
        return True

    s2t = {}
    t2s = {}

    for c1, c2 in zip(s, t):
        if c1 in s2t:
            if s2t[c1] != c2:
                return False
        else:
            s2t[c1] = c2
        
        if c2 in t2s:
            if t2s[c2] != c1:
                return False
        else:
            t2s[c2] = c1
    return True


if __name__ == '__main__':
    # s = "egg"
    # t = "add"
    s = "abba"
    t = "abab"
    res = main(s, t)
    print(res)
