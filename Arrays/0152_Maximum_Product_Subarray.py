# Problem: 152. Maximum Product Subarray
#
# Approach:
# - Use dynamic tracking of:
#   - curr_max: maximum product ending at current index
#   - curr_min: minimum product ending at current index (needed for negative numbers)
# - If current number is negative, swap curr_max and curr_min.
# - Update curr_max and curr_min at each step.
# - Keep track of global maximum product (maxp).
#
# Time Complexity: O(n)
# - Single pass through the array.
#
# Space Complexity: O(1)
# - Only a few variables are used.

class Solution:
    def maxProduct(self, nums):
        maxp = nums[0]
        curr_max = nums[0]
        curr_min = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            if num < 0:
                curr_max, curr_min = curr_min, curr_max

            curr_max = max(num, curr_max * num)
            curr_min = min(num, curr_min * num)

            maxp = max(maxp, curr_max)

        return maxp
