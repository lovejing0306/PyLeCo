# coding=utf-8

def main(nums):
    res  =0
    stack = [0]
    for i in range(1, len(nums)):
        if nums[i] < nums[stack[-1]]:
            stack.append(i)
        elif nums[i] == nums[stack[-1]]:
            stack.pop()
            stack.append(i)
        else:
            r = i
            while len(stack) > 0 and nums[r] > nums[stack[-1]]:
                m = stack.pop()
                if len(stack) > 0:
                    l = stack[-1]
                    h = min(nums[r], nums[l]) - nums[m]
                    w = r-l-1
                    res += (h * w)
            stack.append(i)
    return res


if __name__ == '__main__':
    # height = [0,1,0,2,1,0,1,3,2,1,2,1]
    height = [4,2,0,3,2,5]
    res = main(height)
    print(res)
