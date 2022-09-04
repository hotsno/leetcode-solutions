class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[l] <= nums[m] <= nums[r]:
                return nums[l]
            elif nums[m] <= nums[r]:
                if nums[m - 1] > nums[m]:
                    return nums[m]
                r = m - 1
            else:
                l = m + 1
        return -1
