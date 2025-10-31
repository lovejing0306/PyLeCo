# coding=utf-8

def main(nums1, nums2):
    if len(nums1) == 0 or len(nums2) == 0:
        return 0

    dp = []
    for _ in range(len(nums1)):
        dp.append([0] * len(nums2))
    
    for i in range(len(nums2)):
        if nums1[0] == nums2[i]:
            dp[0][i] = 1
    
    for i in range(len(nums1)):
        if nums1[i] == nums2[0]:
            dp[i][0] = 1
    max_value = 0
    for i in range(1, len(nums1)):
        for j in range(1, len(nums2)):
            if nums1[i] == nums2[j] and nums1[i-1] == nums2[j-1]:  # 只有在连续才记录新的序列长度
                dp[i][j] = dp[i-1][j-1] + 1
            max_value = max(dp[i][j], max_value)
                
    return max_value

if __name__ == '__main__':
    nums1 = [0,0,0,0,0]
    nums2 = [0,0,0,0,0]

    res = main(nums1, nums2)
    print(res)
