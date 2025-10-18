# coding=utf-8
import heapq

class ListNode():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def main(list_nodes):
    if list_nodes is None or len(list_nodes) == 0:
        return None
    
    min_heap = []
   
    for index, node in enumerate(list_nodes):
        if node is not None:
            # 使用该方式实现对类结构类型的数据类型进行 堆排序
            # 其中 index 很重要，相当于是对象的唯一标识符
            heapq.heappush(min_heap, (node.value, index, node))  
    
    head = ListNode(0, None)
    cur = head
    while len(min_heap) > 0:
        _, index, node = heapq.heappop(min_heap)
        if node.next is not None:
            heapq.heappush(min_heap, (node.next.value, index, node.next))  # 复用 index
        cur.next = node
        cur = cur.next
        cur.next = None
    return head.next


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

if __name__ == '__main__':
    # 测试用例：合并3个升序链表
    # 链表1: 1->4->5
    # 链表2: 1->3->4  
    # 链表3: 2->6
    # 期望结果: 1->1->2->3->4->4->5->6
    
    list1 = create_linked_list([1, 4, 5])
    list2 = create_linked_list([1, 3, 4])
    list3 = create_linked_list([2, 6])
    
    list_nodes = [list1, list2, list3]
    
    print("输入的链表:")
    print("链表1:", print_linked_list(list1))
    print("链表2:", print_linked_list(list2))
    print("链表3:", print_linked_list(list3))
    
    # 调用合并函数
    merged_list = main(list_nodes)
    
    print("合并后的链表:", print_linked_list(merged_list))
    print("期望结果: [1, 1, 2, 3, 4, 4, 5, 6]")
    
    # 验证结果
    expected = [1, 1, 2, 3, 4, 4, 5, 6]
    actual = print_linked_list(merged_list)
    if actual == expected:
        print("✅ 测试通过!")
    else:
        print("❌ 测试失败!")
        print(f"期望: {expected}")
        print(f"实际: {actual}")
    