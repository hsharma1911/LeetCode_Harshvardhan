class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        runsum = []
        res = 0
        for i in range(n):
            res+=nums[i]
            runsum.append(res)
        return runsum

