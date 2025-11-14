# coding=utf-8

def main(ss):
    stack = []
    nums = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

    for i in range(len(ss)):
        c = ss[i]
        if c == ']':
            s_ = []
            while len(stack) > 0:
                c_ = stack.pop()
                if c_ == '[':
                    break
                s_.append(c_[::-1])
            
            s_ = ''.join(s_) # 先拼接
            s_ = s_[::-1]  # 执行再次反转
            
            n_ = []
            while len(stack) > 0:
                c_ = stack.pop()
                if c_ not in nums:
                    stack.append(c_)  # 如果不是数字需要再重新添加回去
                    break
                n_.append(c_)
            n_.reverse()
            n_ = ''.join(n_)
            n_ = int(n_)
            
            stack.append(s_ * n_)
        else:
            stack.append(c)
    res = ''.join(stack)
    return res


if __name__ == '__main__':
    s = "abc3[cd]xyz"
    res = main(s)
    print(res)
