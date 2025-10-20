# 217. Contains Duplicate

from typing import List
# Add other common imports here (e.g., from collections import deque)
# from collections import deque 

# Approach: Using a Set for Comparison
# If the lengths aren't equal -> contains duplicate

# Time Complexity: O(n)
# The dominant operation is converting the list to a set, which requires iterating
# through all 'n' elements once.

# Space Complexity: O(n)
# In the worst-case scenario (no duplicates), the set will store 'n' unique elements, 
# requiring space proportional to the input size.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

# --- Local Test Case ---

if __name__ == "__main__":
    solver = Solution()
    
    # Example 1:
    input1 = [1,2,3,1]
    expected1 = True
    result1 = solver.containsDuplicate(input1)
    print(f"Input: {input1}, Output: {result1}, Expected: {expected1}")
    
    # Example 2:
    input2 = [1,2,3,4]
    expected2 = False
    result2 = solver.containsDuplicate(input2)
    print(f"Input: {input2}, Output: {result2}, Expected: {expected2}")

    # Assert check for robustness
    assert result1 == expected1, f"Test 1 Failed: Got {result1}, Expected {expected1}"
    assert result2 == expected2, f"Test 2 Failed: Got {result2}, Expected {expected2}"