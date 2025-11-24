# coding=utf-8

from util import ListNode, print_linked_list, create_linked_list

def main(head, n):
    cur = head

    count = 0
    while cur is not None:
        count += 1
        cur = cur.next
    
    if n > count:
        return head
    elif n == count:
        return head.next
    else:
        root = ListNode(-1)
        root.next = head

        fast = head
        i = 0
        while fast is not None and i< n:
            fast = fast.next
            i+=1

        slow = root
        while fast is not None:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return root.next


if __name__ == '__main__':
    nums = [1,2,3,4,5]
    node = create_linked_list(nums)
    root = main(node, 3)
    res = print_linked_list(root)
    print(res)