class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo<hi:
            mid = (lo+hi)//2
            if mid > 0 and nums[mid] < nums[mid-1]:
                return nums[mid]
            elif nums[mid] < nums[hi]:
                hi = mid - 1  # ans is on the left 
            else:
                lo = mid + 1  # ans is on the right 
        return nums[lo] 