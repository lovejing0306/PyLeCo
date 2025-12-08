# coding=utf-8

def main(nums):
    stack = []
    for num in nums:
        flag = True  # 标记当前行星是否入 栈
        while len(stack) > 0:
            if stack[-1] > 0 and num < 0:  # 只有相向的两颗行星才会发生碰撞
                if abs(stack[-1]) > abs(num):
                    flag = False
                    break
                elif abs(stack[-1]) < abs(num):
                    stack.pop()
                else:
                    stack.pop()
                    flag = False
                    break
            else:
                break
        if flag:
            stack.append(num)
    return stack


if __name__ == '__main__':
    nums = [3,5,-6,2,-1,4]
    res = main(nums)
    print(res)
