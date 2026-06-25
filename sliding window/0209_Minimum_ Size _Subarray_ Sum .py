# Problem: 209. Minimum Size Subarray Sum
#
# Approach:
# - Use two nested loops to check all possible subarrays.
# - Start from each index and keep adding elements until the sum
#   becomes greater than or equal to the target.
# - Record the minimum subarray length found.
# - If no valid subarray exists, return 0.
#
# Time Complexity: O(n²)
# - In the worst case, we examine all possible subarrays.
#
# Space Complexity: O(1)
# - Only a few variables are used.

class Solution:
    def minSubArrayLen(self, target, nums):
        answer = len(nums) + 1

        for i in range(len(nums)):
            total = 0

            for j in range(i, len(nums)):
                total = total + nums[j]

                if total >= target:
                    length = j - i + 1

                    if length < answer:
                        answer = length

                    break

        if answer == len(nums) + 1:
            return 0

        return answer
