# 1929. Concatenation of Array

from typing import List

# Approach: Python List Concatenation
# The problem asks for an array 'ans' which is the concatenation of the input 'nums' with itself.
# In Python, the '+' operator for lists automatically handles this concatenation, creating a new
# list that is nums + nums. This leverages built-in language efficiency.

# Time Complexity: O(n)
# Creating a new list by concatenating two lists of size 'n' requires copying '2n' elements.
# Space Complexity: O(n)
# We allocate new memory proportional to the size of the result (2n), which simplifies to O(n).

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Simple, highly efficient list concatenation.
        return nums + nums
    
# --- Local Test Case ---
if __name__ == "__main__":
    solver = Solution()
    
    # Example 1
    nums1 = [1, 2, 1]
    result1 = solver.getConcatenation(nums1)
    print(f"Input: {nums1}")
    print(f"Output: {result1}")
    print(f"Expected: [1, 2, 1, 1, 2, 1]")
    
    # Example 2
    nums2 = [1, 3, 2, 1]
    result2 = solver.getConcatenation(nums2)
    print(f"Input: {nums2}")
    print(f"Output: {result2}")
    print(f"Expected: [1, 3, 2, 1, 1, 3, 2, 1]")