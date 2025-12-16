# coding=utf-8

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def dfs(node, mapping):
    if node is None:  # 节点为空返回 None
        return None
    if node.val in mapping:
        return mapping[node.val]
    
    new_node = Node(node.val, [])
    mapping[node.val] = new_node
    for neighbor in node.neighbors:
        neighbor_ = dfs(neighbor, mapping)
        new_node.neighbors.append(neighbor_)
    return new_node
    

def main(node):
    mapping = {}  # 使用 mapping 记录克隆的节点
    return dfs(node, mapping)

