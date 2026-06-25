# Problem: 239. Sliding Window Maximum
#
# Approach:
# - Traverse all possible windows of size k.
# - For each window, find its maximum element using max().
# - Store the maximum of each window in the result list.
#
# Time Complexity: O(n × k)
# - There are (n - k + 1) windows, and max(window) takes O(k) time.
#
# Space Complexity: O(k)
# - A temporary window slice of size k is created in each iteration.

class Solution:
    def maxSlidingWindow(self, nums, k):
        res = []

        for i in range(len(nums) - k + 1):
            window = nums[i:i + k]
            res.append(max(window))

        return res
