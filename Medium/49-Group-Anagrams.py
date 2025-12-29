# Problem: 49 - Group Anagrams
# Link: https://leetcode.com/problems/group-anagrams/

from typing import List

# Time:  O(n * m):
# n: the number of strings
# m: the length of the longest string
# Space: O(n)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {} # mapping charCount to a list of Anagrams

        for s in strs:
            count = [0] * 26 # a-z

            for c in s:
                count[ord(c) - ord('a')] += 1
            
            if tuple(count) in res:
                res[tuple(count)].append(s)
            else:
                res[tuple(count)] = []
                res[tuple(count)].append(s)
        
        return list(res.values())

# --- Local Test ---
if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])) # Expected: [["bat"],["nat","tan"],["ate","eat","tea"]]