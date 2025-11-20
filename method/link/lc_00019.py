# coding

from util import create_linked_list, print_linked_list, ListNode


def main(head, n):
    if n == 0:
        return head 

    i=0
    r = head

    while i<n and r is not None:
        r = r.next
        i+=1
    
    if i!=n:
        return head
    
    root = ListNode(-1)
    root.next = head
    l = root
    while r is not None:
        r = r.next
        l = l.next
    l.next = l.next.next
    return root.next


if __name__ == '__main__':
    head = [1,2,3,4,5]
    n = 2

    head = create_linked_list(head)
    node = main(head, n)
    res = print_linked_list(node)
    print(res)
