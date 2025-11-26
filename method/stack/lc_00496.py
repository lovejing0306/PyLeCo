# coding=utf-8

def main(nums1, nums2):
    mapping = {}
    stack = []

    for num in nums2:
        while len(stack) > 0 and stack[-1] < num:
            mapping[stack.pop()] = num
        stack.append(num)
    
    res = []
    for num in nums1:
        val = mapping.get(num, -1)
        res.append(val)
    return res

if __name__ == '__main__':
    # nums1 = [4,1,2]
    # nums2 = [1,3,4,2]
    nums1 = [2,4]
    nums2 = [1,2,3,4]
    res = main(nums1, nums2)
    print(res)