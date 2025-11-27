# coding=utf-8

def main(edges):
    n = len(edges)
    parent = list(range(n + 1))
    in_degree = {}
    
    # 找是否有节点有两个父节点
    conflict = -1
    cycle = -1
    
    for i, (u, v) in enumerate(edges):
        if v in in_degree:
            conflict = i
        else:
            in_degree[v] = i
    
    # 并查集
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return False
        parent[px] = py
        return True
    
    # 如果有冲突的边,先跳过冲突的边
    for i, (u, v) in enumerate(edges):
        if i == conflict:
            continue
        if not union(u, v):  # 如果是 False，说明出现了 环
            cycle = i
            break
    
    # 情况1: 没有节点有两个父节点,说明只是有环
    if conflict == -1:
        return edges[cycle]
    
    # 情况2: 有节点有两个父节点
    # 如果跳过conflict边后没有环,说明conflict边是冗余的
    if cycle == -1:
        return edges[conflict]
    
    # 如果跳过conflict边后还是有环,说明另一条指向该节点的边是冗余的
    return edges[in_degree[edges[conflict][1]]]


if __name__ == '__main__':
    edges = [[1,2],[2,3],[3,4],[4,1],[1,5]]
    res = main(edges)
    print(res)
