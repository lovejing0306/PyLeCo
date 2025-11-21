# coding=utf-8

def main(nums):
    """ 
    双指针实现
    """
    res = []
    if len(nums) == 0:
        return res
    
    i = 0
    j = 1

    while j < len(nums):
        if nums[j] == nums[j-1]+1:
            j+=1
        else:
            if i+1==j:
                res.append(str(nums[i]))
            else:
                res.append(f'{nums[i]}->{nums[j-1]}')
            i=j
            j+=1
    if i + 1==j:
        res.append(str(nums[i]))
    else:
        res.append(f'{nums[i]}->{nums[j-1]}')
    return res


if __name__ == '__main__':
    nums = [0,2,3,4,6,8,9]
    res = main(nums)
    print(res)