# Problem: 5. Longest Palindromic Substring
#
# Approach:
# - Generate all possible substrings using two nested loops.
# - Check whether each substring is a palindrome.
# - If it is a palindrome and longer than the current answer,
#   update the answer.
# - Return the longest palindromic substring found.
#
# Time Complexity: O(n³)
# - There are O(n²) substrings, and checking each palindrome
#   takes O(n) time.
#
# Space Complexity: O(n)
# - Extra space is used to store the current answer.

class Solution:
    def longestPalindrome(self, s):
        ans = ""

        for i in range(len(s)):
            for j in range(i, len(s)):
                part = s[i:j+1]

                if part == part[::-1] and len(part) > len(ans):
                    ans = part

        return ans
