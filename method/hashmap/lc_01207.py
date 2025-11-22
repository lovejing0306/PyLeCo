# coding=utf-8

def main(nums):
    if nums is None or len(nums) == 0:
        return False
    
    counter = {}
    for num in nums:
        if num in counter:
            counter[num] += 1
        else:
            counter[num] = 1
    
    ss = set(counter.values())
    return True if len(counter) == len(ss) else False


if __name__ == '__main__':
    nums = [1,2]
    res = main(nums)
    print(res)
