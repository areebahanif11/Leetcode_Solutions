class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = {}
        first = 0 
        second = 0 
        max_len = 0 
        while second < len(s):
            if count.get(s[second], 0) == 1:
                count[s[first]] = 0
                first += 1 
            else:
                count[s[second]] = 1
                max_len = max(max_len, second - first + 1)
                second += 1
                
        return max_len