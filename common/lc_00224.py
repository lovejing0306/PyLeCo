# coding=utf-8

def main(ss):
    tt = []
    i = 0
    while i < len(ss):
        c = ss[i]
        if c == ' ':
            i+=1
        elif c == '(' or c == ')' or c == '+' or c == '-':
            i+=1
            tt.append(c)
        else:
            num = 0
            j = i
            while j < len(ss) and ss[j].isdigit():
                num = num * 10 + int(ss[j])
                j+=1
            if j!=i:
                tt.append(num)
            i = j
    
    stack = []
    for i in range(len(tt)):
        if tt[i] != ')':
            stack.append(tt[i])
        else:
            stack_ = []
            while len(stack) > 0:
                t_ = stack.pop()
                if t_ == '(':
                    break
                else:
                    stack_.append(t_)
            
            if stack_[-1] == '-':
                a = 0
            else:
                a = stack_.pop()
            while len(stack_) > 0:
                flag = stack_.pop()
                b = stack_.pop()
                a = a + b if flag == '+' else a - b
            stack.append(a)
    
    if len(stack) == 1:
        return stack.pop()
    else:
        stack.reverse()
        if stack[-1] == '-':
            a = 0
        else:
            a = stack.pop()
        while len(stack) > 0:
            flag = stack.pop()
            b = stack.pop()
            a = a+b if flag == '+' else a-b
        return a

if __name__ == '__main__':
    s = '(1+(44+5+2)-3)+(6+8)'
    res = main(s)
    print(res)