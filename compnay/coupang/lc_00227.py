# coding=utf-8

def main(ss):
    stack = []

    i=0
    while i < len(ss):
        if ss[i] == ' ':
            i+=1
        elif ss[i] == '+' or ss[i] == '-':
            stack.append(ss[i])
            i+=1
        elif ss[i] == '*' or ss[i] == '/':
            flag = ss[i]
            a = int(stack.pop())
            i+=1
            tt = []
            while i<len(ss):
                if ss[i] == ' ':
                    pass
                elif ss[i] == '+' or ss[i] == '-' or ss[i] == '*' or ss[i] == '/':
                    break
                else:
                    tt.append(ss[i])
                i+=1
            b = int(''.join(tt))

            if flag == '*':
                c = a * b
            else:
                # LeetCode 227 requires division truncates toward zero
                c = int(a / b)
            stack.append(c)
        else:
            tt = []
            while i < len(ss):
                if ss[i] == ' ':
                    pass
                elif ss[i] == '+' or ss[i] == '-' or ss[i] == '*' or ss[i] == '/':
                    break
                else:
                    tt.append(ss[i])
                i+=1
            a = int(''.join(tt))
            stack.append(a)
    
    # Evaluate remaining + and - from left to right
    if not stack:
        return 0
    res = stack[0]
    j = 1
    while j < len(stack):  # 这里应该从前往后，避免连续减号的情况
        op = stack[j]
        val = stack[j + 1]
        if op == '+':
            res += val
        else:
            res -= val
        j += 2
    return res


if __name__ == '__main__':
    ss = "3+2*2"
    res = main(ss=ss)
    print(res)