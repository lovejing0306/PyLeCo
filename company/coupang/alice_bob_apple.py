# coding=utf-8

def max_apples(apples, k, L):
    """
    Alice 和 Bob 在一个漂亮的果园里面工作，果园里面有N棵苹果树排成了一排，这些苹果树被标记成1 - N号。
    Alice 计划收集连续的K棵苹果树上面的所有苹果，Bob 计划收集连续的L棵苹果树上面的所有苹果。
    他们希望选择不相交的部分（一个由 Alice 的K树组成，另一个由鲍勃 Bob 的L树组成），以免相互干扰。你应该返回他们可以收集的最大数量的苹果。

    N 是整数且在以下范围内：[2，600]
    K 和 L 都是整数且在以下范围内：[1，N-1]
    数组A的每个元素都是以下范围内的整数：[1，500]
    """
    n = len(apples)
    if n < k + L:
        return 0
    
    # 计算每个位置开始的k长度窗口的苹果数
    alice_sum = [0] * (n - k + 1)
    for i in range(n - k + 1):
        alice_sum[i] = sum(apples[i:i + k])
    
    # 计算每个位置开始的L长度窗口的苹果数
    bob_sum = [0] * (n - L + 1)
    for i in range(n - L + 1):
        bob_sum[i] = sum(apples[i:i + L])
    
    max_apples = 0
    
    # Alice的区间在前，Bob的区间在后
    for i in range(len(alice_sum)):
        alice_end = i + k - 1
        # Bob的区间必须从alice_end + 1之后开始
        for j in range(alice_end + 1, n - L + 1):
            max_apples = max(max_apples, alice_sum[i] + bob_sum[j])
    
    # Bob的区间在前，Alice的区间在后
    for i in range(len(bob_sum)):
        bob_end = i + L - 1
        # Alice的区间必须从bob_end + 1之后开始
        for j in range(bob_end + 1, n - k + 1):
            max_apples = max(max_apples, bob_sum[i] + alice_sum[j])
    
    return max_apples


if __name__ == '__main__':
    # 因为Alice 可以选择3-5颗树然后摘到4 + 6 + 3 = 13 个苹果， Bob可以选择7-8棵树然后摘到7 + 4 = 11个苹果，因此他们可以收集到13 + 11 = 24。 
    A = [6, 1, 4, 6, 3, 2, 7, 4] 
    K = 3 
    L = 2 

    res = max_apples(A, K, L)
    print(res)