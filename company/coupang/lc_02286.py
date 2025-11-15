# coding=utf-8

""" 
暴力解码逻辑正确，但是会超时
"""
class BookMyShow:
    def __init__(self, n: int, m: int):
        self.sits = [[0, m] for _ in range(n)]
        self.m = m
        print(self.sits)

    def gather(self, k: int, maxRow: int):
        for i in range(0, maxRow+1):
            start_index, total = self.sits[i]
            if total >= k:
                self.sits[i] = [start_index + k, total - k]
                return [i, start_index]
        
        return []

    def scatter(self, k: int, maxRow: int) -> bool:
        count = 0
        for i in range(0, maxRow + 1):
            _, total = self.sits[i]
            count += total
        if count < k:
            return False
        
        for i in range(0, maxRow + 1):
            start_index, total = self.sits[i]
            if total >= k:
                self.sits[i] = [start_index + k, total - k]
                break
            else:
                self.sits[i] = [self.m, 0]
                k -= total
        return True


if __name__ == '__main__':
    book = BookMyShow(2, 5)
    res = book.gather(4, 0)
    print(res)
    res = book.gather(2, 0)
    print(res)
    res = book.scatter(5, 1)
    print(res)
    res = book.scatter(5, 1)
    print(res)