# coding=utf-8

class Node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def main(head, left, right):
    root = Node(-1)
    root.next = head
    cur = root

    for _ in range(1, left):
        cur = cur.next
    
    pre = cur.next
    cur_ = cur.next.next

    k = right - left
    while cur_ is not None and k > 0:
        t = cur_.next
        pre.next = cur_.next
        cur_.next = cur.next
        cur.next = cur_
        cur_ = t
        k-=1
    return root.next
