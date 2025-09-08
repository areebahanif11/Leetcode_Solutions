class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_first_element(nums, target):
            low, hi, ans = 0, len(nums) - 1, -1
            while low<=hi:
                mid = (low + hi) // 2
                if nums[mid] == target:
                    ans = mid
                    hi = mid - 1 # see if there is more similar elements behind
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    hi = mid - 1
            return ans
        def find_last_element(nums, target):
            low, hi, ans = 0, len(nums) - 1, -1  
            while low<=hi:
                mid = (low+hi) // 2
                if nums[mid] == target:
                    ans = mid
                    low = mid + 1 # see if there is more similar elements on right side 
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    hi = mid - 1
            return ans

        first = find_first_element(nums, target)
        if first == -1:
            return [-1,-1]
        last = find_last_element(nums, target)
        return [first, last]
        