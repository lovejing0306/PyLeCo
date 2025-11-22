# coding=utf-8

def main(nums1, nums2, nums3, nums4):
    v1 = {}
    v2 = {}

    for i in range(len(nums1)):
        for j in range(len(nums2)):
            s = nums1[i] + nums2[j]
            if s in v1:
                v1[s] += 1
            else:
                v1[s] = 1
    
    for i in range(len(nums3)):
        for j in range(len(nums4)):
            s = nums3[i] + nums4[j]
            if s in v2:
                v2[s] += 1
            else:
                v2[s] = 1
    
    count  = 0
    for k, v in v1.items():
        if -k in v2:
            count += v * v2[-k]  # 这里应该相乘，求的是组合数
    return count 


if __name__ == '__main__':
    # nums1 = [1,2]
    # nums2 = [-2,-1]
    # nums3 = [-1,2]
    # nums4 = [0,2]

    nums1 = [0]
    nums2 = [0]
    nums3 = [0]
    nums4 = [0]

    res = main(nums1, nums2, nums3, nums4)
    print(res)