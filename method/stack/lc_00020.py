# coding=utf-8

def main(ss):
    if ss is None or len(ss) == 0:
        return False

    mapping = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    
    stack = []
    for i in range(len(ss)):
        c = ss[i]
        if c == '(' or c == '{' or c == '[':
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            else:
                if stack[-1] == mapping[c]:
                    stack.pop()
                else:
                    return False
    return True if len(stack) == 0 else False


if __name__ == '__main__':
    s = "()[]{}"
    res = main(s)
    print(res)
