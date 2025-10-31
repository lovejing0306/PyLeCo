# coding=utf-8

def main(ss):
    if len(ss) == 0:
        return 0
    if len(ss) == 1:
        return 1
    
    if len(ss) == 2:
        return 3 if ss[0] == ss[1] else 2

    dp = []
    for _ in range(len(ss)):
        dp.append([0] * len(ss))

    count = 0
    for i in range(len(ss)):
        dp[i][i] = 1
        count +=1
    
    for i in range(len(ss)-1):
        if ss[i]==ss[i+1]:
            dp[i][i+1] = 1
            count +=1

    for k in range(2, len(ss)):
        for i in range(len(ss)-k):
            if ss[i] == ss[i+k] and dp[i+1][i+k-1]==1:
                dp[i][i+k] == 1
                count +=1
    return count

if __name__ == '__main__':
    ss = 'cbbd'
    res = main(ss)
    print(res)
