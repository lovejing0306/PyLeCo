# coding=utf-8

"""
链表中倒数第k个节点
"""

class ListNode():
    def __init__(self, value, next_node=None):
        self.value = value 
        self.next = next_node


def main(head, k):
    if head is None:
        return None
    if k <=0:
        return None

    fast = head
    slow = head
    i = 0
    while i<k:
        if fast is None:
            return None
        else:
            fast = fast.next
        i+=1
    
    while fast is not None:
        fast = fast.next
        slow = slow.next
    
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

def find_node_position_from_end(head, target_node):
    """找到目标节点从末尾开始的位置（倒数第几个）"""
    if not head or not target_node:
        return -1
    
    # 先计算链表总长度
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    
    # 找到目标节点的正向位置
    current = head
    position = 0
    while current:
        if current is target_node:
            return length - position  # 返回倒数位置
        current = current.next
        position += 1
    return -1

if __name__ == '__main__':
    print("=== 链表中倒数第k个节点 测试用例 ===\n")
    
    # 测试用例1: 正常情况 - 链表[1,2,3,4,5]，倒数第2个节点
    print("测试用例1: 正常情况 - 倒数第2个节点")
    list1 = create_linked_list([1, 2, 3, 4, 5])
    print("输入链表:", print_linked_list(list1))
    print("k = 2")
    result1 = main(list1, 2)
    if result1:
        pos1 = find_node_position_from_end(list1, result1)
        print(f"倒数第2个节点值: {result1.value}, 验证位置: 倒数第{pos1}个")
        print("期望: 值=4, 倒数第2个")
        print("✅ 测试通过!" if result1.value == 4 and pos1 == 2 else "❌ 测试失败!")
    else:
        print("❌ 测试失败! 返回None")
    print()
    
    # 测试用例2: 正常情况 - 链表[1,2,3,4,5]，倒数第3个节点
    print("测试用例2: 正常情况 - 倒数第3个节点")
    list2 = create_linked_list([1, 2, 3, 4, 5])
    print("输入链表:", print_linked_list(list2))
    print("k = 3")
    result2 = main(list2, 3)
    if result2:
        pos2 = find_node_position_from_end(list2, result2)
        print(f"倒数第3个节点值: {result2.value}, 验证位置: 倒数第{pos2}个")
        print("期望: 值=3, 倒数第3个")
        print("✅ 测试通过!" if result2.value == 3 and pos2 == 3 else "❌ 测试失败!")
    else:
        print("❌ 测试失败! 返回None")
    print()
    
    # 测试用例3: 边界情况 - 倒数第1个节点（最后一个）
    print("测试用例3: 边界情况 - 倒数第1个节点")
    list3 = create_linked_list([1, 2, 3, 4, 5])
    print("输入链表:", print_linked_list(list3))
    print("k = 1")
    result3 = main(list3, 1)
    if result3:
        pos3 = find_node_position_from_end(list3, result3)
        print(f"倒数第1个节点值: {result3.value}, 验证位置: 倒数第{pos3}个")
        print("期望: 值=5, 倒数第1个")
        print("✅ 测试通过!" if result3.value == 5 and pos3 == 1 else "❌ 测试失败!")
    else:
        print("❌ 测试失败! 返回None")
    print()
    
    # 测试用例4: 边界情况 - 倒数第5个节点（第一个）
    print("测试用例4: 边界情况 - 倒数第5个节点（链表长度）")
    list4 = create_linked_list([1, 2, 3, 4, 5])
    print("输入链表:", print_linked_list(list4))
    print("k = 5")
    result4 = main(list4, 5)
    if result4:
        pos4 = find_node_position_from_end(list4, result4)
        print(f"倒数第5个节点值: {result4.value}, 验证位置: 倒数第{pos4}个")
        print("期望: 值=1, 倒数第5个")
        print("✅ 测试通过!" if result4.value == 1 and pos4 == 5 else "❌ 测试失败!")
    else:
        print("❌ 测试失败! 返回None")
    print()
    
    # 测试用例5: 单节点链表
    print("测试用例5: 单节点链表")
    list5 = create_linked_list([42])
    print("输入链表:", print_linked_list(list5))
    print("k = 1")
    result5 = main(list5, 1)
    if result5:
        pos5 = find_node_position_from_end(list5, result5)
        print(f"倒数第1个节点值: {result5.value}, 验证位置: 倒数第{pos5}个")
        print("期望: 值=42, 倒数第1个")
        print("✅ 测试通过!" if result5.value == 42 and pos5 == 1 else "❌ 测试失败!")
    else:
        print("❌ 测试失败! 返回None")
    print()
    
    # 测试用例6: 异常情况 - k超出链表长度
    print("测试用例6: 异常情况 - k超出链表长度")
    list6 = create_linked_list([1, 2, 3])
    print("输入链表:", print_linked_list(list6))
    print("k = 5 (超出链表长度3)")
    result6 = main(list6, 5)
    print(f"结果: {result6}")
    print("期望: None")
    print("✅ 测试通过!" if result6 is None else "❌ 测试失败!")
    print()
    
    # 测试用例7: 异常情况 - k为0
    print("测试用例7: 异常情况 - k为0")
    list7 = create_linked_list([1, 2, 3])
    print("输入链表:", print_linked_list(list7))
    print("k = 0")
    result7 = main(list7, 0)
    print(f"结果: {result7}")
    print("期望: None")
    print("✅ 测试通过!" if result7 is None else "❌ 测试失败!")
    print()
    
    # 测试用例8: 异常情况 - k为负数
    print("测试用例8: 异常情况 - k为负数")
    list8 = create_linked_list([1, 2, 3])
    print("输入链表:", print_linked_list(list8))
    print("k = -1")
    result8 = main(list8, -1)
    print(f"结果: {result8}")
    print("期望: None")
    print("✅ 测试通过!" if result8 is None else "❌ 测试失败!")
    print()
    
    # 测试用例9: 异常情况 - 空链表
    print("测试用例9: 异常情况 - 空链表")
    list9 = None
    print("输入链表: None")
    print("k = 1")
    result9 = main(list9, 1)
    print(f"结果: {result9}")
    print("期望: None")
    print("✅ 测试通过!" if result9 is None else "❌ 测试失败!")
    print()
    
    print("=== 算法说明 ===")
    print("使用双指针法（快慢指针）:")
    print("1. 快指针先向前移动k步")
    print("2. 然后快慢指针同时移动，直到快指针到达链表末尾")
    print("3. 此时慢指针指向的就是倒数第k个节点")
    print("4. 时间复杂度: O(n), 空间复杂度: O(1)")
    print("5. 边界条件处理: k<=0, k>链表长度, 空链表等情况返回None")
    