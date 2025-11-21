# coding=utf-8
from util import ListNode

def method_1(head):
    visited = {}
    i = 0

    cur = head
    while cur is not None:
        if cur in visited:
            return cur
        visited[cur] = i
        i += 1
        cur = cur.next
    return None

def method_2(head):
    slow = head
    fast = head

    flag = False
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            flag = True
            break
    if flag:
        count = 0  # 记录环中节点的数量
        while fast.next is not slow:
            count +=1
            fast = fast.next
        count += 1
        slow = head
        fast = head
        while count > 0:  # fast 指针先走 count 步
            fast = fast.next
            count -= 1
        while slow is not fast:
            slow = slow.next
            fast = fast.next
        return slow
    else:
        return None
    

if __name__ == '__main__':
    head = ListNode(-1)
    method_1(head)
