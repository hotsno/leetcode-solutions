from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)

        res = 0
        for node in graph:
            if node not in visited:
                dfs(node)
                res += 1

        return res
