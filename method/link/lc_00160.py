# coding=utf-8

from util import create_linked_list, print_linked_list, ListNode

def main(head_a, head_b):
    if head_a is None or head_b is None:
        return None
    
    num_a = 0
    num_b = 0

    cur_a = head_a
    cur_b = head_b

    while cur_a is not None:
        num_a+=1
        cur_a = cur_a.next
    
    while cur_b is not None:
        num_b += 1
        cur_b = cur_b.next
    
    if num_a > num_b:
        t = num_a - num_b
        i = 0
        while head_a is not None and i<t:
            head_a = head_a.next
            i+=1
    elif num_a < num_b:
        t = num_b - num_a
        i = 0
        while head_b is not None and i<t:
            head_b = head_b.next
            i+=1
    while head_a is not None and head_b is not None:
        if head_a is head_b:
            return head_a
        head_a = head_a.next
        head_b = head_b.next
    return None
