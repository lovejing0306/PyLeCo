# coding=utf-8

from util import create_linked_list, print_linked_list

def main(head):
    if head is None:
        return None

    cur = head
    pre = None

    while cur is not None:
        cur_ = cur
        cur = cur.next
        cur_.next = pre
        pre = cur_
    return pre


if __name__ == '__main__':
    nums = [1,2,3,4,5]
    head = create_linked_list(nums)
    root = main(head)

    res = print_linked_list(root)
    print(res)