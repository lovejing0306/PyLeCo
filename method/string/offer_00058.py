# coding=utf-8

def main(s, k):
    if s is None or len(s) == 0:
        return s
    n = len(s)
    k = k % n
    if k == 0:
        return s
    s1 = s[:k][::-1]
    s2 = s[k:][::-1]
    s = s1 + s2
    s = s[::-1]
    return s


if __name__ == '__main__':
    s = 'abcdefg'
    k = 2
    res = main(s, k)
    print(res)
