# coding=utf-8

def main(g, s):
    if len(s) == 0:
        return 0

    count = 0
    i = len(s) - 1
    j = len(g) - 1

    while i >= 0 and j >= 0:
        if s[i] >= g[j]:
            count += 1
            i -= 1
            j -= 1
        else:
            j -= 1
    return count


if __name__ == '__main__':
    g = [1,2]
    s = [1,2,3]

    res = main(g, s)
    print(res)
    