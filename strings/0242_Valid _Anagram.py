# Problem: 242. Valid Anagram
#
# Approach:
# - Sort both strings.
# - If the sorted strings are equal, they are anagrams.
# - Otherwise, they are not anagrams.
#
# Time Complexity: O(n log n)
# - Sorting each string takes O(n log n).
#
# Space Complexity: O(n)
# - Extra space is used for the sorted strings.

class Solution:
    def isAnagram(self, s, t):
        if sorted(s) == sorted(t):
            return True
        else:
            return False
