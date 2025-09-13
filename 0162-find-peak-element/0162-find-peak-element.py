class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1 ]:
                left = mid + 1   # move to the right
            else:
                right = mid      # move to the left
        return left              # here in this condition left and right become equal so we can return any variable when we find peak
