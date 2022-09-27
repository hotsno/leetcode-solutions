class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        level = []
        rotten = set()
        num_oranges = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    level.append((r, c))
                    rotten.add((r, c))
                if grid[r][c] != 0:
                    num_oranges += 1

        if num_oranges == 0:
            return 0
        
        depth = 0
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while level:
            depth += 1
            next = []
            for r, c in level:
                for r_off, c_off in dirs:
                    r_new, c_new = r + r_off, c + c_off
                    if (r_new in range(rows)
                            and c_new in range(cols)
                            and grid[r_new][c_new] != 0
                            and (r_new, c_new) not in rotten):
                        rotten.add((r_new, c_new))
                        next.append((r_new, c_new))
            level = next
            
        if len(rotten) != num_oranges:
            return -1
        return depth - 1
