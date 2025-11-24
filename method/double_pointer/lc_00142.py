# coding=utf-8


def main(head):
    if head is None:
        return None
    
    fast = head
    slow = head

    flag = False
    while fast.next is not None and fast.next.next is not None:
        fast = fast.next.next 
        slow = slow.next
        if fast is slow:
            flag = True
            break
    
    if flag is False:
        return None
    
    count = 1
    fast = fast.next
    while fast is not slow:
        count += 1
        fast = fast.next
    
    fast = head
    slow = head
    i = 0
    while i<count:
        fast = fast.next
        i+=1
    while slow is not fast:
        slow = slow.next
        fast = fast.next
    return slow 
