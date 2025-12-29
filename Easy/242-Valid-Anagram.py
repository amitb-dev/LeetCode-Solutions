# Problem: 242 - Valid Anagram
# Link: https://leetcode.com/problems/valid-anagram/

from typing import List

# Time:  O(n)
# Space: O(1)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        counter = {}
        for ch in s:
            counter[ch] = counter.get(ch, 0) + 1
            
        for ch in t:
            if ch not in counter or counter[ch] == 0:
                return False
            counter[ch] -= 1
            
        return True

# --- Local Test ---
if __name__ == "__main__":
    s = Solution()
    print(s.isAnagram("anagram", "nagaram")) # Expected: True