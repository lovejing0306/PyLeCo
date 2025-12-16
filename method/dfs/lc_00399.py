# coding=utf-8

def dfs(mapping, a, b, visited, res, index):
    if a == b:
        return True  # 如果找到了目标值，则返回 true
    visited.add(a)
    for item in mapping[a]:
        k, v = item
        if k in visited:
            continue
        res[index] *= v  # 做累积来计算表达式
        if dfs(mapping, k, b, visited, res, index):
            return True
        res[index] /= v
    return False


def main(equations, values, queries):
    """ 
    - 把 equations 构造成有向带权图：
    - A -> B 权重 value
    - B -> A 权重 1/value
    - 对每个查询 C/D 用 DFS 寻找路径，并通过乘积得到比例 ！！！
    """
    mapping = {}   # 记录等式之间相互的计算的结果
    for equ, val in zip(equations, values):
        a, b = equ
        if a in mapping:
            mapping[a].append((b, val))
        else:
            mapping[a] = [(b, val)]
        
        if b in mapping:
            mapping[b].append((a, 1/val))
        else:
            mapping[b] = [(a, 1/val)]
   
    res = [1] * len(queries)   # 初始化结果列表
    for idx, que in enumerate(queries):
        a, b = que
        if a in mapping and b in mapping: # 如果两个符号同时存在
            visited = set()
            if dfs(mapping, a, b, visited, res, idx) is False:
                res[idx] = -1.
        else:
            res[idx] = -1.
    return res


if __name__ == '__main__':
    # equations = [["a","b"],["b","c"]]
    # values = [2.0,3.0]
    # queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

    # equations = [["a","b"],["b","c"],["bc","cd"]]
    # values = [1.5,2.5,5.0]
    # queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]

    equations = [["a","b"]]
    values = [0.5]
    queries = [["a","b"],["b","a"],["a","c"],["x","y"]]

    res = main(equations, values, queries)
    print(res)