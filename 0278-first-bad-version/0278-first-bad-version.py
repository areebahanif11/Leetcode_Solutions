# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# LeetCode already knows which version is the first bad one.
# LeetCode has a hidden variable called bad.

# For example, bad = 4.
# This is how isBadVersion(version) works:
# If version >= bad → returns True.
# If version < bad → returns False.

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        hi = n
        first_bad_version = -1 
        while low<=hi:
            mid = (low+hi) // 2
            if isBadVersion(mid):
                first_bad_version = mid
                hi = mid - 1
            else:
                low = mid + 1

        return first_bad_version


        