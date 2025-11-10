# coding=utf-8

class Node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def main(head, val):
    root = Node(0, None)

    cur = root

    while head is not None:
        if head.val == val:
            head = head.next
        else:
            head_ = head
            head = head.next
            head_.next = None
            
            cur.next = head_
            cur = cur.next

    return root.next


def print_node(node):
    while node is not None:
        print(node.val)
        node = node.next

if __name__ == '__main__':
    [1,2,6,3,4,5,6]
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(6)
    node4 = Node(3)
    node5 = Node(4)
    node6 = Node(5)
    node7 = Node(6)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7

    # print_node(node1)

    node = main(node1, 6)
    print_node(node)
