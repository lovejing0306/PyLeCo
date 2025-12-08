# coding=utf-8

def main(nums):
    res = [0] * len(nums)
    stack = [0]
    
    for i in range(1, len(nums)):
        while len(stack) > 0 and nums[stack[-1]] < nums[i]:
            index = stack.pop()
            res[index] = i-index
        stack.append(i)
    return res

if __name__ == '__main__':
    nums = [73,74,75,71,69,72,76,73]
    res = main(nums)
    print(res)
