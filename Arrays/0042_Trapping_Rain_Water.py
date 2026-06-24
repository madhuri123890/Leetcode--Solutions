# Problem: 42. Trapping Rain Water
#
# Approach:
# - Use two pointers: left and right.
# - Maintain:
#   - left_max: highest bar seen from left side
#   - right_max: highest bar seen from right side
# - At each step, move the smaller side inward:
#   - If current height is smaller than max, water is trapped.
# - Add trapped water at each position.
#
# Time Complexity: O(n)
# - Each index is visited at most once.
#
# Space Complexity: O(1)
# - Only a few variables are used.

class Solution:
    def trap(self, height):
        left = 0
        right = len(height) - 1

        left_max = 0
        right_max = 0

        water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1

        return water
