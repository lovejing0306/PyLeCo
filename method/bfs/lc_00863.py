# coding=utf-8

class TreeNode():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(node, mapping):
    if node is None:
        return None
    l = dfs(node.left, mapping)
    r = dfs(node.right, mapping)
    if l is not None:
        if node.val in mapping:
            mapping[node.val].append(l)
        else:
            mapping[node.val] = [l]
        if l in mapping:
            mapping[l].append(node.val)
        else:
            mapping[l] = [node.val]
    if r is not None:
        if node.val in mapping:
            mapping[node.val].append(r)
        else:
            mapping[node.val] = [r]
        if r in mapping:
            mapping[r].append(node.val)
        else:
            mapping[r] = [node.val]

    return node.val

def main(root, target, k):
    if k == 0:
        return [target.val]
    mapping = {}
    dfs(root, mapping)  # 关键点获取树中相邻节点之间的依赖关系
    
    queue = [target.val]
    count = 0
    visited = {target.val}

    while len(queue) > 0:
        new_queue = []
        for val in queue:
            for sub in mapping.get(val, []):
                if sub not in visited:
                    visited.add(sub)
                    new_queue.append(sub)
        queue = new_queue
        count += 1
        if count == k:
            break
    
    return queue if count == k else []


if __name__ == '__main__':
    node0 = TreeNode(0)
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)

    node3.left = node5
    node3.right = node1
    node5.left = node6
    node5.right = node2
    node1.left = node0
    node1.right = node8
    node2.left = node7
    node2.right = node4

    res = main(node3, target = node5, k = 2)
    print(res)
