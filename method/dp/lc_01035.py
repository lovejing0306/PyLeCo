# coding=utf-8

from re import I, L


def main(nums1, nums2):
    if len(nums1) == 0 or len(nums2) == 0:
        return 0
    
    dp = []
    for _ in range(len(nums1)):
        dp.append([0]*len(nums2))
    
    for i in range(len(nums1)):
        if nums1[i] == nums2[0]:
            while i<len(nums1):
                dp[i][0] = 1
                i+=1
            break
    for i in range(len(nums2)):
        if nums1[0] == nums2[i]:
            while i<len(nums2):
                dp[0][i] = 1
                i+=1
            break

    for i in range(1, len(nums1)):
        for j in range(1, len(nums2)):
            if nums1[i] == nums2[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(max(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1])
    return dp[len(nums1)-1][len(nums2)-1]


if __name__ == '__main__':
    nums1 = [1,3,7,1,7,5]
    nums2 = [1,9,2,5,1]
    res = main(nums1, nums2)
    print(res)
