# coding=utf-8


class ListNode():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def main(head):
    if head is None:
        return None
    slow = head
    fast = head
    # 由于偶数个元素是，要选取靠后的一个作为中间节点，所以要直接从 fast 是否是 None 开始判断
    while fast is not None and fast.next is not None:   
        slow = slow.next
        fast = fast.next.next

    return slow


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

def find_node_position(head, target_node):
    """找到目标节点在链表中的位置（从0开始）"""
    if not head or not target_node:
        return -1
    current = head
    position = 0
    while current:
        if current is target_node:
            return position
        current = current.next
        position += 1
    return -1


if __name__ == '__main__':
    print("=== LeetCode 876: 链表的中间结点 测试用例 ===\n")
    
    # 测试用例1: 奇数长度链表 [1,2,3,4,5]
    print("测试用例1: 奇数长度链表")
    list1 = create_linked_list([1, 2, 3, 4, 5])
    print("输入链表:", print_linked_list(list1))
    middle1 = main(list1)
    middle_pos1 = find_node_position(list1, middle1)
    print(f"中间节点值: {middle1.value}, 位置: {middle_pos1}")
    print("期望: 值=3, 位置=2 (奇数长度时返回正中间的节点)")
    print("✅ 测试通过!" if middle1.value == 3 and middle_pos1 == 2 else "❌ 测试失败!")
    print()
    
    # 测试用例2: 偶数长度链表 [1,2,3,4,5,6]
    print("测试用例2: 偶数长度链表")
    list2 = create_linked_list([1, 2, 3, 4, 5, 6])
    print("输入链表:", print_linked_list(list2))
    middle2 = main(list2)
    middle_pos2 = find_node_position(list2, middle2)
    print(f"中间节点值: {middle2.value}, 位置: {middle_pos2}")
    print("期望: 值=4, 位置=3 (偶数长度时返回第二个中间节点)")
    print("✅ 测试通过!" if middle2.value == 4 and middle_pos2 == 3 else "❌ 测试失败!")
    print()
    
    # 测试用例3: 单节点链表 [1]
    print("测试用例3: 单节点链表")
    list3 = create_linked_list([1])
    print("输入链表:", print_linked_list(list3))
    middle3 = main(list3)
    middle_pos3 = find_node_position(list3, middle3)
    print(f"中间节点值: {middle3.value}, 位置: {middle_pos3}")
    print("期望: 值=1, 位置=0")
    print("✅ 测试通过!" if middle3.value == 1 and middle_pos3 == 0 else "❌ 测试失败!")
    print()
    
    # 测试用例4: 两节点链表 [1,2]
    print("测试用例4: 两节点链表")
    list4 = create_linked_list([1, 2])
    print("输入链表:", print_linked_list(list4))
    middle4 = main(list4)
    middle_pos4 = find_node_position(list4, middle4)
    print(f"中间节点值: {middle4.value}, 位置: {middle_pos4}")
    print("期望: 值=2, 位置=1 (两个节点时返回第二个)")
    print("✅ 测试通过!" if middle4.value == 2 and middle_pos4 == 1 else "❌ 测试失败!")
    print()
    
    # 测试用例5: 较长的奇数链表 [1,2,3,4,5,6,7]
    print("测试用例5: 较长的奇数链表")
    list5 = create_linked_list([1, 2, 3, 4, 5, 6, 7])
    print("输入链表:", print_linked_list(list5))
    middle5 = main(list5)
    middle_pos5 = find_node_position(list5, middle5)
    print(f"中间节点值: {middle5.value}, 位置: {middle_pos5}")
    print("期望: 值=4, 位置=3")
    print("✅ 测试通过!" if middle5.value == 4 and middle_pos5 == 3 else "❌ 测试失败!")
    print()
    
    # 测试用例6: 空链表
    print("测试用例6: 空链表")
    list6 = None
    print("输入链表: None")
    middle6 = main(list6)
    print(f"中间节点: {middle6}")
    print("期望: None")
    print("✅ 测试通过!" if middle6 is None else "❌ 测试失败!")
    print()
    
    print("=== 算法说明 ===")
    print("使用快慢指针法（Floyd's Tortoise and Hare）:")
    print("- 慢指针每次移动1步，快指针每次移动2步")
    print("- 当快指针到达链表末尾时，慢指针正好在中间位置")
    print("- 对于偶数长度的链表，返回第二个中间节点")
    print("- 时间复杂度: O(n), 空间复杂度: O(1)")

