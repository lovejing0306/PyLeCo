# coding=utf-8

def main(ss):
    if ss is None or len(ss) <=1:
        return ss
    
    stack = []
    for i in range(len(ss)):
        c = ss[i]
        if len(stack) > 0 and stack[-1] == c:
            while len(stack) > 0 and stack[-1] == c:
                stack.pop()
        else:
            stack.append(c)
    return ''.join(stack)


if __name__ == '__main__':
    ss = 'abbaca'
    res = main(ss)
    print(res)

