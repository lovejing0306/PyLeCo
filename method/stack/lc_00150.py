# coding=utf-8

def main(tokens):
    stack = []

    for token in tokens:
        if token == '+':
            a = stack.pop()
            b = stack.pop()
            c = a + b
            stack.append(c)
        elif token == '-':
            a = stack.pop()
            b = stack.pop()
            c = b - a
            stack.append(c)
        elif token == '*':
            a = stack.pop()
            b = stack.pop()
            c = a * b
            stack.append(c)
        elif token == '/':
            a = stack.pop()
            b = stack.pop()
            c = int(b/a)
            stack.append(c)
        else:
            stack.append(int(token))
    return stack.pop()


if __name__ == '__main__':
    tokens = ["2","1","+","3","*"]
    res = main(tokens)
    print(res)