# coding=utf-8

def main(s):
    items = s.split(' ')
    res = [item for item in items if item !=' ' and item !='']
    res.reverse()
    return ' '.join(res)


if __name__ == '__main__':
    s = 'a good   example'
    res = main(s)
    print(res)