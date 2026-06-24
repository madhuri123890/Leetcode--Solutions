# Problem: 217. Contains Duplicate
#
# Approach:
# - Iterate through the array using two nested loops.
# - Compare each element with every element that comes after it.
# - If any two elements are equal, return True.
# - If no duplicate elements are found after all comparisons, return False.
#
# Time Complexity: O(n²)
# Space Complexity: O(1)

class Solution:
    def containsDuplicate(self, nums):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        else:
            return False
