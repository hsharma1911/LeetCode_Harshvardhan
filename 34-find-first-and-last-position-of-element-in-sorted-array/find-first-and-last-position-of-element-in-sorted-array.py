class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        first, last = -1, -1

        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                first = mid  
                last = mid  
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if first != -1:
            left, right = first, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                
                if nums[mid] == target:
                    last = mid  
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

        return [first, last]