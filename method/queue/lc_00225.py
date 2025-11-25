# coding=utf-8
import queue

class MyStack:
    def __init__(self):
        self.queue1 = queue.Queue()
        self.queue2 = queue.Queue()

    def push(self, x: int) -> None:
        if self.queue1.qsize() == 0 and self.queue2.qsize() == 0:
            self.queue1.put(x)
        elif self.queue1.qsize() == 0:
            self.queue2.put(x)
        elif self.queue2.qsize() == 0:
            self.queue1.put(x)

    def pop(self) -> int:
        if self.queue1.qsize() == 0:
            while self.queue2.qsize() > 1:
                self.queue1.put(self.queue2.get())
            return self.queue2.get()
        elif self.queue2.qsize() == 0:
            while self.queue1.qsize() > 1:
                self.queue2.put(self.queue1.get())
            return self.queue1.get()

    def top(self) -> int:
        if self.queue1.qsize() == 0:
            print('111')
            while self.queue2.qsize() > 1:
                self.queue1.put(self.queue2.get())
            a = self.queue2.get()
            self.queue1.put(a)
            return a
        elif self.queue2.qsize() == 0:
            while self.queue1.qsize() > 1:
                self.queue2.put(self.queue1.get())
            a = self.queue1.get()
            self.queue2.put(a)
            return a
        
    def empty(self) -> bool:
        if self.queue1.qsize() == 0 and self.queue2.qsize() == 0:
            return True
        else:
            return False
        
if __name__ == '__main__':
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    param_2 = obj.top()
    param_3 = obj.pop()
    param_4 = obj.empty()
    print(param_2)
    print(param_3)