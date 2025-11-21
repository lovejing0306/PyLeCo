# coding=utf-8

def main(s, t):
    if len(s) != len(t):
        return False

    ss = [0] * 26
    tt = [0] * 26

    for s_ in s:
        ss[ord(s_)-ord('a')] += 1
    
    for t_ in t:
        tt[ord(t_)-ord('a')] += 1
    
    for i, j in zip(ss, tt):
        if i!=j:
            return False
    return True


if __name__ == '__main__':
    s = "rat"
    t = "car"

    res = main(s, t)
    print(res)
