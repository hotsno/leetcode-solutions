class Solution:
    def rob(self, nums: List[int]) -> int:
        pp, p = 0, 0
        for n in nums:
            temp = max(pp + n, p)
            pp = p
            p = temp
        return p
