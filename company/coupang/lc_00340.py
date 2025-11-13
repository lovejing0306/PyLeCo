# coding=utf-8

def main(ss, k):
    """
    最多有K个不同字符的最长子串

    Given a string, find the length of the longest substring T that contains at most k distinct characters.

    Example 1:
    Input: s = "eceba", k = 2
    Output: 3
    Explanation: T is "ece" which its length is 3.
    
    Example 2:
    Input: s = "aa", k = 1
    Output: 2
    Explanation: T is "aa" which its length is 2.
    """
    counter = {}
    max_l = 0
    j = 0
    for i in range(len(ss)):
        c = ss[i]
        if c in counter:
            counter[c] +=1
        else:
            counter[c] = 1
        
        while len(counter) > k:
            c = ss[j]
            counter[c] -= 1
            if counter[c] == 0:
                del counter[c]
            j+=1
        max_l = max(max_l, i-j+1)  # 由于题目要求的是最多不超过 k 个字符
    return max_l


if __name__ == '__main__':
    s = "aa"
    k = 1

    res = main(s, k=k)
    print(res)