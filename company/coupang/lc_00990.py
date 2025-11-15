# coding=utf-8

parent = list(range(26))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    parent[find(x)] = find(y)

def main(equations):
    """
    使用 并查集 的方案
    """
    for ss in equations:
        if ss[1] == '=':
            x = ord(ss[0])-ord('a')
            y = ord(ss[3])-ord('a')
            union(x, y)
    
    for ss in equations:
        if ss[1] == '!':
            x = ord(ss[0])-ord('a')
            y = ord(ss[3])-ord('a')
            if find(x) == find(y):
                return False
    return True


def method2(equations):
    """
    使用 回溯的方案
    """
    def dfs(eqs, visited, cur, target):
        """ 
        通过回溯的方法查看是否能够从 cur 到 target
        """
        if cur == target:
            return True
        if cur not in eqs:
            return False
        for cc in eqs[cur]:
            if cc in visited:
                continue
            visited.add(cc)
            if dfs(eqs, visited, cc, target):
                return True
        return False

    # 访问所有的等式，构建图
    eqs = {}
    for ss in equations:
        if ss[1] == '=':
            x = ss[0]
            y = ss[3]

            if x not in eqs:
                eqs[x] = []
            if y not in eqs:
                eqs[y] = []
            
            eqs[x].append(y)
            if x!=y:
                eqs[y].append(x)
    # 访问所有的不等式
    for ss in equations:
        if ss[1] == '!':
            x = ss[0]
            y = ss[3]

            visited = {x}
            if dfs(eqs, visited, x, y):
                return False
    return True

        
if __name__ == '__main__':
    ss = ["a!=a"]
    res = method2(ss)
    print(res)
