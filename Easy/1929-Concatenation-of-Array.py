# Problem: 1929 - Concatenation of Array
# Link: https://leetcode.com/problems/concatenation-of-array/

from typing import List

# Time:  O(n)
# Space: O(n)

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums

# --- Local Test ---
if __name__ == "__main__":
    s = Solution()
    print(s.getConcatenation([1, 2, 1])) # Expected: [1, 2, 1, 1, 2, 1]