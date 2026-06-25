# Problem: 567. Permutation in String
#
# Approach:
# - Check every substring of s2 with the same length as s1.
# - Sort the substring and s1.
# - If the sorted values are equal, a permutation of s1 exists in s2.
# - If no matching substring is found, return False.
#
# Time Complexity: O((n - m + 1) × m log m)
# - n = length of s2, m = length of s1.
# - Each substring of length m is sorted and compared.
#
# Space Complexity: O(m)
# - Extra space is used for creating and sorting the substring.

class Solution:
    def checkInclusion(self, s1, s2):
        length = len(s1)

        for i in range(0, len(s2) - length + 1):
            part = s2[i:i + length]

            if sorted(part) == sorted(s1):
                return True

        return False
