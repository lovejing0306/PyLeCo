# coding=utf-8

def main(ss):
    if len(ss) <2:
        return 0
    # 第一步，标记哪些位置是有效的括号
    flags = [False] * len(ss)
    stack = []
    for i in range(len(ss)):
        c = ss[i]
        if c == '(':
            stack.append(i)
        else:
            if len(stack) > 0 and ss[stack[-1]] == '(':
                flags[stack.pop()] = True
                flags[i] = True
            else:
                stack.append(i)
    # 使用 双指针 找出最长有效括号
    res = 0
    l = 0
    while l<len(flags):
        if flags[l] is False:
            l+=1
        else:
            r = l+1
            while r < len(flags) and flags[r]:
                r+=1
            res = max(res, r-l)
            l = r
    return res



if __name__ == '__main__':
    s = ')()())'
    res = main(s)
    print(res)