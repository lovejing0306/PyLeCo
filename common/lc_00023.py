# coding=utf-8
import heapq

class Node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def main(nodes):
    heap = []
    
    for i, node in enumerate(nodes):
        if node is None:
            continue
        # 将 i 放在第二个位置是为了在堆比较出现相同值时使用一个可比较的整数作为“次级键”，
        heapq.heappush(heap, (node.val, i, node))
    
    head = Node(-1)
    cur = head

    while len(heap) > 0:
        _, index, node = heapq.heappop(heap)
        if node.next is not None:
            heapq.heappush(heap, (node.next.val, index, node.next))
        node.next = None
        cur.next = node
        cur = cur.next
    return head.next
