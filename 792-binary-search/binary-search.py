class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n= len(nums)
        idx =-1
        s, e = 0,n
        while s<e:
            m = s+ (e-s)//2
            if nums[m]==target:
                idx = m
                break
            elif target<nums[m]:
                e=m
            else:
                s=m+1
        return idx
        