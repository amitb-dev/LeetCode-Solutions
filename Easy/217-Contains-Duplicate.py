# Problem: 217 - Contains Duplicate
# Link: https://leetcode.com/problems/contains-duplicate/

from typing import List

# Time:  O(n)
# Space: O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

# --- Local Test ---
if __name__ == "__main__":
    s = Solution()
    print(s.containsDuplicate([1, 2, 3, 1])) # Expected: True
    print(s.containsDuplicate([1, 2, 3, 4])) # Expected: False