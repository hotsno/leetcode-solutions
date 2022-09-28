class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, l, s):
            if s == target:
                res.append(l.copy())
                return
            if i >= len(candidates) or s > target:
                return
            l.append(candidates[i])
            dfs(i, l, s + candidates[i])
            l.pop()
            dfs(i + 1, l, s)
        dfs(0, [], 0)
        return res
