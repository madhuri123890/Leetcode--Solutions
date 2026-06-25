# Problem: 76. Minimum Window Substring
#
# Approach:
# - Generate all possible substrings using two nested loops.
# - For each substring, check if it contains all characters of t
#   with the required frequencies.
# - Keep track of the smallest valid substring found.
# - Return the smallest substring, or an empty string if none exists.
#
# Time Complexity: O(n³)
# - Generating all substrings takes O(n²).
# - Checking character counts for each substring adds extra work.
#
# Space Complexity: O(n)
# - Extra space is used to store the current substring and answer.

class Solution:
    def minWindow(self, s, t):
        ans = ""

        for i in range(len(s)):
            for j in range(i, len(s)):
                sub = s[i:j + 1]
                good = True

                for ch in t:
                    if sub.count(ch) < t.count(ch):
                        good = False

                if good:
                    if ans == "":
                        ans = sub
                    elif len(sub) < len(ans):
                        ans = sub

        return ans
