# coding=utf-8

def main(nums1, nums2):
    a = set()
    for num in nums1:
        a.add(num)
    res = []
    b = set()
    for num in nums2:
        if num in a and num not in b:
            res.append(num)
            b.add(num)

    return res

if __name__ == '__main__':
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]

    res = main(nums1, nums2)
    print(res)
