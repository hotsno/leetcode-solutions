class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        rows, cols = len(grid), len(grid[0])
        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or grid[r][c] == '0' or (r, c) in seen:
                return
            seen.add((r, c))
            dfs(r - 1, c)
            dfs(r, c - 1)
            dfs(r + 1, c)
            dfs(r, c + 1)

        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != '0' and (r, c) not in seen:
                    dfs(r, c)
                    res += 1
        return res
