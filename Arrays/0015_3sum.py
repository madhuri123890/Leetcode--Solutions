# Problem: 15. 3Sum
#
# Approach:
# - Sort the array first.
# - Fix one element using index i.
# - Use two pointers (j, k) to find pairs such that:
#   nums[i] + nums[j] + nums[k] == 0
# - Skip duplicate elements to avoid repeated triplets.
# - Move pointers based on sum comparison.
#
# Time Complexity: O(n^2)
# - Outer loop runs n times.
# - Two-pointer scan runs in O(n) for each i.
#
# Space Complexity: O(1) (excluding output list)
# - No extra data structures used.

class Solution:
    def threeSum(self, nums):
        nums.sort()
        ans = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                s = nums[i] + nums[j] + nums[k]

                if s == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

                elif s < 0:
                    j += 1
                else:
                    k -= 1

        return ans
