# Problem: 560. Subarray Sum Equals K
#
# Approach:
# - Use a brute force method with two nested loops.
# - Fix a starting index i.
# - Expand the subarray from i to j while maintaining running sum (total).
# - If at any point total == k, increment count.
# - Repeat for all starting positions and return total count.
#
# Time Complexity: O(n²)
# - Outer loop runs n times.
# - Inner loop runs up to n times for each i.
#
# Space Complexity: O(1)
# - Only variables are used, no extra data structures.

class Solution:
    def subarraySum(self, nums, k):
        count = 0

        for i in range(len(nums)):
            total = 0

            for j in range(i, len(nums)):
                total = total + nums[j]

                if total == k:
                    count = count + 1

        return count
