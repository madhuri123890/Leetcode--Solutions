# Problem: 11. Container With Most Water
#
# Approach:
# - Use two pointers: left at start, right at end.
# - Calculate area using:
#   width = right - left
#   height = min(height[left], height[right])
# - Update maximum area.
# - Move the pointer with smaller height inward (to try and increase area).
#
# Time Complexity: O(n)
# - Each element is visited at most once using two pointers.
#
# Space Complexity: O(1)
# - Only variables are used.

class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            current_area = min(height[left], height[right]) * width
            max_area = max(max_area, current_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
