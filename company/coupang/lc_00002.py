# coding=utf-8

class Node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def main(node1, node2):
    head = Node(0)
    cur = head

    a = 0
    
    while node1 is not None and node2 is not None:
        s = node1.val + node2.val + a
        a = s // 10
        val = s % 10

        node = Node(val)
        cur.next = node
        cur = cur.next

        node1 = node1.next
        node2 = node2.next
    
    while node1 is not None:
        s = node1.val + a
        a = s // 10
        val = s % 10

        node = Node(val)
        cur.next = node
        cur = cur.next
        node1 = node1.next

    while node2 is not None:
        s = node2.val + a
        a = s // 10
        val = s % 10

        node = Node(val)
        cur.next = node
        cur = cur.next

        node2 = node2.next

    if a != 0:
        node = Node(a)
        cur.next = node
    
    return head.next

def print_link(node):
    while node is not None:
        print(node.val)
        node = node.next
    print('='*30)


if __name__ == '__main__':
    node0_1 = Node(2)
    node0_2 = Node(4)
    node0_3 = Node(3)

    node0_1.next = node0_2
    node0_2.next = node0_3

    node1_1 = Node(5)
    node1_2 = Node(6)
    node1_3 = Node(4)

    node1_1.next = node1_2
    node1_2.next = node1_3

    print_link(node0_1)
    print_link(node1_1)

    node = main(node0_1, node1_1)
    print_link(node)
