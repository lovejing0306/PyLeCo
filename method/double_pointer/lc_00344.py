# coding=utf-8

def main(s):
    if s is None or len(s) == 0:
        return s
    s = list(s)    # 由于 python 中的字符串是不可变对象，为了最替换操作，必须转成 list 类型
    i = 0
    j = len(s)-1
    while i<j:
        # t = s[i]
        # s[i] = s[j]
        # s[j] = t
        s[i], s[j] = s[j], s[i]
        i+=1
        j-=1
    s = ''.join(s)
    return s


if __name__ == '__main__':
    s = '12345'
    print(main(s))