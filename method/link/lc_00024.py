# coding=utf-8
from util import create_linked_list, print_linked_list

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def main(head):
    new_head = ListNode(-1)
    new_head.next = head

    prev = new_head
    cur = head
    while cur is not None and cur.next is not None :
        next__ = cur.next.next
        cur.next.next = None
        prev.next = cur.next
        prev = prev.next
        prev.next = cur
        prev = prev.next
        prev.next = next__

        cur = next__
    return new_head.next


if __name__ == '__main__':
    vals = [1,2,3,4]
    head = create_linked_list(vals)

    root = main(head)
    res = print_linked_list(root)
    print(res)
