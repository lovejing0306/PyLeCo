# coding=utf-8
from util import create_linked_list, print_linked_list

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


def method_2(head):
    l = None
    r = head

    while r is not None:
        cur = r
        r = r.next

        cur.next = l
        l = cur
    return l


if __name__ == '__main__':
    values = [0,1,2,3,4]
    head = create_linked_list(values)

    # cur = main(head)
    cur = method_2(head)
    print(print_linked_list(cur))