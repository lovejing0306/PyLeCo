# coding=utf-8

def main(ss):
    dp = []
    for _ in range(len(ss)):
        dp.append([False] * len(ss))
    
    res = None
    for i in range(len(ss)):
        dp[i][i] = True
        res = ss[i]
    
    for i in range(1, len(ss)):
        if ss[i] == ss[i-1]:
            dp[i-1][i] = True
            res = ss[i-1: i+1]
    
    for i in range(2, len(ss)):
        for j in range(len(ss)-i):
            if ss[j] == ss[j+i] and dp[j+1][j+i-1]:
                dp[j][j+i] = True
                res = ss[j: j+i+1]

    return res


if __name__ == '__main__':
    s = 'babad'
    res = main(s)
    print(res)