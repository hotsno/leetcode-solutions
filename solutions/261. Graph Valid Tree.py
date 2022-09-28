from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        def dfs(node, prev):
            if node in visited:
                return False
            for neighbor in graph[node]:
                if neighbor is prev:
                    continue
                if not dfs(neighbor, node):
                    return False
            return True

        return dfs(0, -1) and n == len(visited)
