# coding=utf-8

def main(ss):
    # 第一步：去除空格，将字符数字转为整数
    tt = []
    i = 0
    while i < len(ss):
        c = ss[i]
        if c == ' ': 
            i+=1
        elif c == '(' or c == ')' or c == '+' or c == '-':
            tt.append(c)
            i+=1
        else:
            j = i+1
            while j < len(ss) and ss[j].isdigit():
                j+=1
            num = int(ss[i:j])
            tt.append(num)
            i = j

    # 第二步：开始执行运算
    stack = []
    for i in range(len(tt)):
        c = tt[i]
        if c == ')':
            stack_ = []
            while len(stack) > 0:
                c_ = stack.pop()
                if c_ == '(':
                    break
                else:
                    stack_.append(c_)
            # 可以将 4+5+2 拆解为 4，+5， +2
            if stack_[-1] == '-':  # 小的 trick
                x = 0
            else:
                x = stack_.pop()
            while len(stack_) > 0:
                flag = stack_.pop()
                y = stack_.pop()
                x = x + y if flag == '+' else x - y
            stack.append(x)
        else:
            stack.append(c)
    
    stack.reverse()
    if stack[-1] == '-':
        x = 0
    else:
        x = stack.pop()
    while len(stack) > 0:
        flag = stack.pop()
        y = stack.pop()
        x = x + y if flag == '+' else x - y
    return x

if __name__ == '__main__':
    s = "(1+(4+5+2)-3)+(6+8)"
    res = main(s)
    print(res)