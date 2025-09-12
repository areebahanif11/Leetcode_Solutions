class Solution:
    def _find_pivot_index(self, nums: List[int]) -> int:
        """
        Helper method to find the index of the smallest element (the pivot).
        """
        left, right = 0, len(nums) - 1
        
        # If the list is not rotated, the first element is the smallest.
        if nums[left] <= nums[right]:
            return 0

        while left <= right:
            mid = (left + right) // 2
            # The pivot is the only element smaller than its predecessor
            if mid > 0 and nums[mid] < nums[mid - 1]:
                return mid
            # If mid is in the "larger" part of the array, pivot is to the right
            if nums[mid] >= nums[right]:
                left = mid + 1
            # Otherwise, pivot is to the left
            else:
                right = mid - 1
        return left

    def _binary_search(self, nums: List[int], target: int, left: int, right: int) -> int:
        """
        Helper method for a standard binary search on a given range.
        """
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def search(self, nums: List[int], target: int) -> int:
    #   method that orchestrates the search.
        
        if not nums:
            return -1

        n = len(nums)
        pivot_idx = self._find_pivot_index(nums)

        # First, handle the simple case: the array was not rotated.
        # This now correctly returns the result.
        if pivot_idx == 0:
            return self._binary_search(nums, target, 0, n - 1)

        # For a rotated array, decide the search space based on the first element.
        # This logic is now correct for all edge cases, including target == nums[0].
        if target >= nums[0]:
            # Target is in the first, larger-valued section.
            return self._binary_search(nums, target, 0, pivot_idx - 1)
        else:
            # Target is in the second, smaller-valued section.
            return self._binary_search(nums, target, pivot_idx, n - 1)

   