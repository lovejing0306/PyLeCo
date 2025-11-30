# coding=utf-8

def main(moves):
    mapping = {
        'R':(1, 0),
        'L':(-1, 0),
        'U':(0, 1),
        'D':(0, -1)
    }

    s = [0, 0]
    for i in range(len(moves)):
        c = mapping[moves[i]]
        s[0] += c[0]
        s[1] += c[1]
    if s[0] == 0 and s[1] == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    ss = 'LL'
    res = main(ss)
    print(res)