class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')
        summ = 0 
        left = 0
        for right in range(len(nums)):
            summ += nums[right]
            while summ >= target:
                min_length = min(min_length, right - left + 1)
                summ -= nums[left]
                left += 1
        return min_length if min_length < float('inf') else 0
        