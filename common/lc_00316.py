# coding=utf-8

def main(ss):
    stack = []  # 记录结果
    visited = set()  # 记录已经访问过的字符
    # 记录每个字符最后出现的索引位置
    last_index = {char:i for i,char in enumerate(ss)}

    for i, char in enumerate(ss):
        if char in visited:
            pass  # 如果字符已经被访问过，则直接跳过
        else:
            # 如果 栈中存在元素，并且栈顶元素大于当前字符，并且栈顶元素在后面也会出现
            while len(stack)>0 and stack[-1] > char and i < last_index[stack[-1]]:
                # 则弹出栈顶元素
                c_ = stack.pop()
                visited.discard(c_)  # 同时，从访问过的集合中删除该元素
            stack.append(char)  # 将当前字符加入 栈
            visited.add(char)   # 将当前字符加入 访问集合
    return ''.join(stack)


if __name__ == '__main__':
    s = 'bcabc'
    res = main(s)
    print(res)
