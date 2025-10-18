# coding=utf-8

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


class ListNode():
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


last_node = ListNode(-1, None)

def dfs(node):
    if node is None:
        global last_node
        return last_node
    temp = dfs(node.next)
    temp.next = node
    node.next = None
    return node


def main(head):
    dfs(head)
    return last_node.next


if __name__ == '__main__':
    values = [0,1,2,3,4]
    head = create_linked_list(values)

    cur = main(head)
    print(print_linked_list(cur))