# coding=utf-8

from collections import defaultdict


class Solution:
    def sumOfDistancesInTree(self, n, edges):
        """
        树中距离之和
        对于树中的每个节点,计算它到其他所有节点的距离之和
        
        思路:
        1. 第一次DFS:以0为根,计算每个节点的子树节点数和到子树所有节点的距离和
        2. 第二次DFS:通过换根DP,从父节点推导子节点的答案
           - 当根从parent移到child时:
             - child子树中的节点距离减1(closer)
             - 其他节点距离加1(farther)
             - ans[child] = ans[parent] - count[child] + (n - count[child])
        """
        # 构建邻接表
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # count[i]: 以i为根的子树的节点数
        # ans[i]: 节点i到其子树所有节点的距离和
        count = [1] * n
        ans = [0] * n
        
        def dfs1(node: int, parent: int) -> None:
            """第一次DFS: 计算子树信息"""
            for child in graph[node]:
                if child == parent:
                    continue
                dfs1(child, node)
                count[node] += count[child]
                ans[node] += ans[child] + count[child]
        
        def dfs2(node: int, parent: int) -> None:
            """第二次DFS: 换根DP"""
            for child in graph[node]:
                if child == parent:
                    continue
                # 从node换到child作为根
                # child子树的count[child]个节点距离-1
                # 其余(n - count[child])个节点距离+1
                ans[child] = ans[node] - count[child] + (n - count[child])
                dfs2(child, node)
        
        dfs1(0, -1)
        dfs2(0, -1)
        
        return ans


# 测试用例
if __name__ == "__main__":
    solution = Solution()
    
    # 测试1: n=6, edges=[[0,1],[0,2],[2,3],[2,4],[2,5]]
    n1 = 6
    edges1 = [[0,1],[0,2],[2,3],[2,4],[2,5]]
    print(solution.sumOfDistancesInTree(n1, edges1))  # [8,12,6,10,10,10]
    
    # 测试2: n=1, edges=[]
    n2 = 1
    edges2 = []
    print(solution.sumOfDistancesInTree(n2, edges2))  # [0]
    
    # 测试3: n=2, edges=[[1,0]]
    n3 = 2
    edges3 = [[1,0]]
    print(solution.sumOfDistancesInTree(n3, edges3))  # [1,1]