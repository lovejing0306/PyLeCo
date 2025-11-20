# coding=utf-8

class ListNode():
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

def create_linked_list(values):
    """根据值列表创建链表"""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def print_linked_list(head):
    """打印链表"""
    result = []
    current = head
    while current:
        result.append(current.value)
        current = current.next
    return result
