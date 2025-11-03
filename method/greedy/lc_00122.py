# coding=utf-8

def main(prices):
    count = 0
    if len(prices) < 2:
        return count
    
    for i in range(1, len(prices)):
        sub_ = prices[i] - prices[i-1]   # 只要前后两天有收益就能够交易
        if sub_ > 0:
            count += sub_
    
    return count

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    res = main(prices)
    print(res)
