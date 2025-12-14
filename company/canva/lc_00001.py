# coding=utf-8

def dfs(node, mapping, path):
    path.append(node)
    sub_nodes = mapping[node]
    if len(sub_nodes) == 0:
        return
    
    for sub_node in sub_nodes:
        dfs(sub_node, mapping, path)


def main(mapping):
    """ 
    input: 
    {
    "pizza" : ["dough", "tomato"],
    "dough": [],
    "tomato": []
    }
    output: ["tomato", "dough", "pizza"] or ["dough", "tomato", "pizza"]

    input: 
    {
    "flour" : [],
    "dough" : ["flour"],
    "pizza" : ["dough"],
    "tomato": ['dough']
    }
    output: ["flour", "dough", "pizza"], ["flour", "dough", "tomato"]
    
    input: 
    {
    "pizza" : ["dough", "tomato"],
    "dough": ["flour", "water"],
    "tomato": [],
    "water": [],
    "flour": []
    }
    possible outputs: 
    ["flour", "water", "dough", "tomato", "pizza"]
    ["water", "flour", "dough", "tomato", "pizza"]
    ["flour", "water", "tomato", "dough", "pizza"]
    ["water", "flour", "tomato", "dough", "pizza"]
    ["flour", "tomato", "water", "dough", "pizza"]
    ["water", "tomato", "flour", "dough", "pizza"]
    ["tomato", "flour", "water", "dough", "pizza"]
    ["tomato", "water", "flour", "dough", "pizza"]

    约束：
    1. 没有给定起始的类
    2. 
    """
    dep = {}
    for key, nodes in mapping.items():
        dep[key] = 0
        for node in nodes:
            dep[node] = 0
    
    for key, nodes in mapping.items():
        for node in nodes:
            dep[node] = 1

    for node, val in dep.items():
        if val == 0:
            path = []
            # node = 'pizza'
            dfs(node, mapping, path)
            path.reverse()
            print(path)


if __name__ == '__main__':
    mapping = {
        "pizza" : ["dough", "tomato"],
        "dough": ["flour", "water"],
        "tomato": [],
        "water": [],
        "flour": []
    }
    main(mapping)