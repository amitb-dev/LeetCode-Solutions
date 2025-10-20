# 242. Valid Anagram

from typing import List, Optional
# Add other common imports here (e.g., from collections import deque)
# from collections import deque 

# Approach: Character Frequency Counting (Hash Map)
# We count the frequency of each character in the first string (s) and store it in a hash map.
# We then iterate through the second string (t), decrementing the counts. If we encounter 
# a character not in the map, or if a count drops below zero, the strings are not anagrams.
# The lengths must also be checked upfront for an early exit.

# Time Complexity: O(n)
# We iterate through both strings, s and t, which is O(n) + O(n) = O(n), where n is the length of the strings.

# Space Complexity: O(1)
# The alphabet size is constant (26 lowercase English letters). The space required for the 
# frequency map is bounded by this constant size, making the space complexity O(1).

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counts = {}

        for char in s:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
        
        for char in t:
            if char in counts:
                if counts[char] == 0:
                    return False
                else:
                    counts[char] -= 1
            else:
                return False
        
        return True



# --- Local Test Case ---

if __name__ == "__main__":
    solver = Solution()
    
    # Example 1:
    input1 = "anagram"
    input1_2 = "nagaram"
    expected1 = True
    result1 = solver.isAnagram(input1, input1_2)
    print(f"Input: {input1} {input1_2}, Output: {result1}, Expected: {expected1}")
    
    # Example 2:
    input2 = "rat"
    input2_2 = "car"
    expected2 = False
    result2 = solver.isAnagram(input2, input2_2)
    print(f"Input: {input2} {input2_2}, Output: {result2}, Expected: {expected2}")
    
    