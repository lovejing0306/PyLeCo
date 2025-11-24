# coding=utf-8

def main(ss):
    words = ss.split()
    words = [w for w in words if w !='' and w!=' ']
    words.reverse()
    return ' '.join(words)

if __name__ == '__main__':
    ss = 'a good example'
    res = main(ss)
    print(res)