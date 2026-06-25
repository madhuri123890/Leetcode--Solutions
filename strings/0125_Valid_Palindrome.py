# Problem: 125. Valid Palindrome
#
# Approach:
# - Convert the string to lowercase.
# - Remove all non-alphanumeric characters.
# - Compare the cleaned string with its reverse.
# - If both are equal, return True; otherwise, return False.
#
# Time Complexity: O(n)
# - We traverse the string once to build the cleaned string and once to reverse/compare it.
#
# Space Complexity: O(n)
# - Extra space is used to store the cleaned string.

class Solution:
    def isPalindrome(self, s):
        s = s.lower()
        new = ""

        for ch in s:
            if ch.isalnum():
                new += ch

        if new == new[::-1]:
            return True
        else:
            return False
