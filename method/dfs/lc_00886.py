# coding=utf-8

def main(n, dislikes):
    # 初始化图结构 邻接表矩阵
    graph = [[] for _ in range(n+1)]
    # 使用不能够出现在同一组中的节点对初始化 邻接表
    for a, b in dislikes:
        graph[a].append(b)
        graph[b].append(a)
    # 初始化颜色数组，0 表示未染色，1和-1表示两种不同的颜色
    colors = [0] * (n+1)  

    def dfs(node, color):
        colors[node] = color
        # 访问当前节点相邻的节点
        for neighboor in graph[node]:
            # 如果当前节点和相邻节点染上了相同的颜色，则直接返回 false
            if colors[neighboor] == color:
                return False
            # 如果相邻节点没有被染色，并且相邻节点的染色结果返回 false，则直接返回 false
            if colors[neighboor] == 0 and dfs(neighboor, -color) is False: # -color 表示给相邻节点染上相反的颜色
                return False
        # 如果所有的相邻节点都被正常染色，则直接返回 true
        return True

    for i in range(1, n+1):  # 从节点 1 开始遍历
        if colors[i] == 0: # 如果节点没有被染色，则开启深度递归
            if dfs(i, 1) is False:
                return False
    return True


if __name__ == '__main__':
    # n = 4
    # dislikes = [[1,2],[1,3],[2,4]]
    n = 5
    dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]

    res = main(n, dislikes)
    print(res)