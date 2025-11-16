# coding=utf-8

class Node():
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

def main(head):
    root = Node(-1)
    mapping = {}
    cur_new = root
    cur_old = head

    while cur_old is not None:
        tt = Node(cur_old.val)
        cur_new.next = tt
        cur_new = cur_new.next
        mapping[cur_old] = tt
        cur_old = cur_old.next
    
    cur_new = root.next
    cur_old = head
    while cur_old is not None:
        if cur_old.random is not None:
            cur_new.random = mapping[cur_old.random]
        cur_old = cur_old.next
        cur_new = cur_new.next
    return root.next

