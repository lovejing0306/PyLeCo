# coding=utf-8
import heapq

def main(array, k):
    if array is None or len(array) == 0:
        return None
    if k < 0:
        return None

    min_heap = []   # 最小堆的堆顶元素小于所有其它节点的值
    i = 0
    while i<len(array):
        if i < k:   # 将前 k 个元素直接放入到 最小堆 中
            heapq.heappush(min_heap, array[i])
        else:
            # 从 第 k+1 个元素开始
            if min_heap[0] < array[i]:  # 如果最小堆的堆顶元素小于数组中的当前元素，说明此时遇到了更大的元素
                heapq.heappop(min_heap)  # 则弹出堆顶元素
                heapq.heappush(min_heap, array[i])  # 将新的元素压入到最小堆
        i+=1
    return min_heap[0]


if __name__ == '__main__':
    a = [4,3,7,2,6,8]
    k = 3
    print(main(a, k=k))
