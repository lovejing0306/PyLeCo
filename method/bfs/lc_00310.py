# coding=utf-8

def method_1(n, edges):
    """ 
    这种解法会超时
    """
    if n==1:
        return [0]
    mapping = {}
    for edge in edges:
        a, b = edge
        if a in mapping:
            mapping[a].append(b)
        else:
            mapping[a] = [b]
        if b in mapping:
            mapping[b].append(a)
        else:
            mapping[b] = [a]
        
    counter = [0] * n
    min_val = float('inf')
    for key in mapping.keys():
        queue = [key]
        visited = {key}
        count = 0

        while len(queue) > 0:
            new_queue = []
            for node in queue:
                for sub_node in mapping[node]:
                    if sub_node not in visited:
                        visited.add(sub_node)
                        new_queue.append(sub_node)
            queue = new_queue
            if len(queue) > 0:
                count += 1
        min_val = min(min_val, count)
        counter[key] = count
    res = []
    for i in range(len(counter)):
        if counter[i] == min_val:
            res.append(i)
    return res

def method_2(n, edges):
    """ 
    最优解法，逐层拨洋葱
    """
    if n == 1:  # 如果只有一个 节点 直接返回 0
        return [0]

    graph = [set() for _ in range(n)]  # 记录每个节点的相邻节点
    degree = [0] * n  # 记录每个节点的 度
    for a, b in edges:
        graph[a].add(b)
        graph[b].add(a)
        degree[a] += 1
        degree[b] += 1
    # 把度为 1 的节点，也就是 叶子节点 加入到 集合中
    leaves = [i for i in range(n) if degree[i] == 1]
    remaining = n  # 记录剩余节点
    while remaining > 2:
        remaining -= len(leaves)  # 当前总的节点数量减去 叶子节点的数量
        new_leaves = []
        for leaf in leaves:  # 访问每个叶子节点
            for neighbor in list(graph[leaf]):  # 访问每个叶子节点的邻居
                graph[neighbor].remove(leaf)  # 从叶子的节点邻居节点中删除该叶子节点
                degree[neighbor] -= 1  # 将邻居节点的度 减 1
                if degree[neighbor] == 1: # 如果邻居节点的 度 为 1，说明其变成了新的叶子节点
                    new_leaves.append(neighbor)   # 加入新的叶子节点列表
                degree[leaf] = 0  # 将叶子节点的 度 归为 0
                graph[leaf].clear()  # 清空叶子节点的列表
        leaves = new_leaves
    return leaves


if __name__ == '__main__':
    n = 6
    edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
    # n = 4
    # edges = [[1,0],[1,2],[1,3]]

    res = method_1(n, edges)
    print(res)