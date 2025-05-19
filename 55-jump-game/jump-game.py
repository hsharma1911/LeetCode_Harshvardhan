class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxindex = 0
        for i in range (len(nums)):
            if i > maxindex:
                return False
            maxindex = max(maxindex, i+nums[i])
        return True