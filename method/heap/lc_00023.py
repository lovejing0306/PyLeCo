# coding=utf-8

import heapq

class ListNode():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def main(lists):
    heap = []
    head = ListNode(-1)
    cur = head

    for i in range(len(lists)):
        node = lists[i]
        if node is not None:
            # 如果 val 重复，可以使用 i 执行判断
            heapq.heappush(heap, (node.val, i, node))
    
    while len(heap) > 0:
        _, i, node = heapq.heappop(heap)
        node_next = node.next
        cur.next = node
        cur = cur.next
        cur.next = None
        if node_next is not None:
            heapq.heappush(heap, (node_next.val, i, node_next))
    return head.next


if __name__ == '__main__':
    pass