class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(houses):
            r1, r2 = 0, 0
            for house in houses:
                temp = max(r1 + house, r2)
                r1 = r2
                r2 = temp
            return r2
        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))
