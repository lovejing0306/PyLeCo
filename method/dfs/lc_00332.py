# coding=utf-8

def dfs(graph, name, res):
    while len(graph.get(name, [])) > 0:
        sub_name = graph[name].pop(0)  # 弹出之后可以保证每张机票只使用一次！！！
        dfs(graph, sub_name, res)
    res.append(name)  # 必须在最后往 res 中添加航班
    

def main(tickets):
    graph = {}
    for ticket in tickets:
        src, dst = ticket
        if src in graph:
            graph[src].append(dst)
        else:
            graph[src] = [dst]
    
    for key in graph.keys():
        graph[key].sort()

    res = []
    dfs(graph, 'JFK', res)
    res = res[::-1]   # 必须做翻转
    return res


if __name__ == '__main__':
    # tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    res = main(tickets)
    print(res)
