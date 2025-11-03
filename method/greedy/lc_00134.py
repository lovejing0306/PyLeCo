# coding=utf-8

def main(gas, cost):
    start = 0
    sum_ = 0
    cur_ = 0

    for i in range(len(gas)):
        sum_ += (gas[i] - cost[i])
        cur_ += (gas[i] - cost[i])
        if cur_ < 0:    # 判断当前剩油量
            cur_ = 0
            start = i + 1
    
    if sum_ < 0:
        return -1
    return start


if __name__ == '__main__':
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]

    res = main(gas, cost)
    print(res)