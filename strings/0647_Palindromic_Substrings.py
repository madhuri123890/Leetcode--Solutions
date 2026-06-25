# Problem: 647. Palindromic Substrings
#
# Approach:
# - Generate all possible substrings using two nested loops.
# - Check if each substring is a palindrome by comparing it
#   with its reverse.
# - If it is a palindrome, increase the count.
# - Return the total number of palindromic substrings.
#
# Time Complexity: O(n³)
# - There are O(n²) substrings, and checking each palindrome
#   takes O(n) time.
#
# Space Complexity: O(n)
# - Extra space is used when creating substrings and their reverse.

class Solution:
    def countSubstrings(self, s):
        count = 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    count += 1

        return count
