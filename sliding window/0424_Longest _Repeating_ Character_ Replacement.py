# Problem: 424. Longest Repeating Character Replacement
#
# Approach:
# - Use a sliding window with two pointers (left and right).
# - Count the frequency of characters in the current window.
# - If the number of characters to replace exceeds k, shrink the window.
# - Keep track of the maximum valid window length.
#
# Time Complexity: O(n)
# - Each character is added to and removed from the window at most once.
#
# Space Complexity: O(1)
# - The frequency dictionary stores at most 26 uppercase English letters.

class Solution:
    def characterReplacement(self, s, k):
        left = 0
        ans = 0
        count = {}

        for right in range(len(s)):
            if s[right] in count:
                count[s[right]] += 1
            else:
                count[s[right]] = 1

            max_freq = max(count.values())

            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
                max_freq = max(count.values())

            ans = max(ans, right - left + 1)

        return ans
