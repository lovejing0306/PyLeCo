# coding=utf-8

def main(ss):
    if len(ss) == 0:
        return 0

    visited = {}   # 记录访问过的字符

    res = 1
    r = 0
    l = 0
    # 对于最长无重复的字符串来说，字典中记录的无重复的字符个数等于两个指针之间的字符个数
    while l < len(ss):
        c = ss[l]
        if c in visited:
            visited[c] += 1
        else:
            visited[c] = 1
        
        while len(visited) != (l-r+1):
            visited[ss[r]] -= 1
            if visited[ss[r]] == 0:
                del visited[ss[r]]
            r+=1
        
        res = max(res, l-r + 1)
        l+=1
    return res


if __name__ == '__main__':
    s = 'pwwkew'
    res = main(s)
    print(res)
