# Problem: 3. Longest Substring Without Repeating Characters
#
# Approach:
# - Use two nested loops to generate all possible substrings.
# - Start from each index and keep adding characters until a duplicate is found.
# - Track the length of the longest substring without repeating characters.
#
# Time Complexity: O(n²)
# - The outer loop runs n times, and the inner loop may scan up to n characters.
#
# Space Complexity: O(n)
# - The temporary substring can grow up to length n.

class Solution:
    def lengthOfLongestSubstring(self, s):
        max_length = 0

        for i in range(len(s)):
            substring = ""

            for j in range(i, len(s)):
                if s[j] in substring:
                    break
                else:
                    substring = substring + s[j]

            if len(substring) > max_length:
                max_length = len(substring)

        return max_length
