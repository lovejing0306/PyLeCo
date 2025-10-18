# coding=utf-8

def main(array):
    stack = []

    for value in array:
        flag = True
        while len(stack) > 0:
            if stack[-1] > 0 and value <0:
                if abs(value) > abs(stack[-1]):
                    stack.pop()
                else:
                    flag = False
                    break
            else:
                break
        if flag:
            stack.append(value)
    
    return stack


if __name__ == '__main__':
    # a = [-2,-1,1,2]
    a = [5,10,-5]
    print(main(a))