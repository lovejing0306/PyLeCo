# coding=utf-8

import threading

class FizzBuzz():
    def __init__(self, n):
        self.n = n
        self.cur = 1
        # 锁使用能保证原子性，但无法保证公平性和高效性
        self.lock = threading.Lock()  # 创建一个线程锁
    
    def fizz(self):
        while True:
            with self.lock:  # 执行每个方法的时候先把锁加上
                if self.cur > self.n:
                    return 
                if self.cur % 3 == 0 and self.cur % 5!= 0:
                    print('fizz')
                    self.cur += 1
    def buzz(self):
        while True:
            with self.lock:  # 执行每个方法的时候先把锁加上
                if self.cur > self.n:
                    return 
                if self.cur % 3!=0 and self.cur % 5 == 0:
                    print('buzz')
                    self.cur += 1
    
    def fizzbuzz(self):
        while True:
            with self.lock:  # 执行每个方法的时候先把锁加上
                if self.cur > self.n:
                    return
                if self.cur % 3==0 and self.cur % 5 == 0:
                    print('fizzbuzz')
                    self.cur += 1
    def number(self):
        while True:
            with self.lock:  # 执行每个方法的时候先把锁加上
                if self.cur > self.n:
                    return
                if self.cur % 3!=0 and self.cur % 5 != 0:
                    print(self.cur)
                    self.cur += 1
                
