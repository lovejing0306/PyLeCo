# coding=utf-8

def dfs(graph, colors, node, color):
    colors[node] = color
    for neighboor in graph[node]:
        if colors[neighboor] == color:
            return False
        if colors[neighboor] == 0:
            if dfs(graph, colors, neighboor, -color) is False:
                return False
    return True


def main(graph):
    colors = [0] * len(graph)

    for i in range(len(graph)):
        if colors[i] == 0:
            if dfs(graph, colors, i, 1) is False:
                return False
    return True


if __name__ == '__main__':
    graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
    res = main(graph)
    print(res)
