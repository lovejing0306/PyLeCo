# coding=utf-8

def main(nums):
    """ 
    遍历两次
    """
    res = [-1] * len(nums)

    stack = []
    for i in range(len(nums)):
        while len(stack) > 0 and nums[i] > nums[stack[-1]]:
            res[stack.pop()] = nums[i]
        stack.append(i)
    
    for i in range(len(nums)):
        while len(stack) > 0 and nums[i] > nums[stack[-1]]:
            index = stack.pop()
            if res[index] == -1:
                res[index] = nums[i]
        stack.append(i)
    return res


if __name__ == '__main__':
    nums = [1,2,3,4,3]
    res = main(nums)
    print(res)
