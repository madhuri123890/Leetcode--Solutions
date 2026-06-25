# Problem: 162. Find Peak Element
#
# Approach:
# - Use Binary Search to find a peak element.
# - Find the middle element and compare it with the next element.
# - If nums[mid] < nums[mid + 1], the peak lies on the right side.
# - Otherwise, the peak lies on the left side (including mid).
# - Continue until left == right, which is the index of a peak.
#
# Time Complexity: O(log n)
# - The search space is halved in each iteration.
#
# Space Complexity: O(1)
# - Only a few variables are used.

class Solution:
    def findPeakElement(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left
