# Problem: 53. Maximum Subarray
#
# Approach:
# - Use Kadane’s Algorithm.
# - At each index, decide whether to:
#   1) start a new subarray from current element
#   2) extend the previous subarray by adding current element
# - Maintain:
#   - current_sum: maximum sum of subarray ending at current index
#   - max_sum: maximum sum found overall
# - Update both while traversing the array.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def maxSubArray(self, nums):
        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)

        return max_sum
