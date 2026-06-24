# Problem: Two Sum
# Approach:
# - Check every pair of numbers using two nested loops.
# - If the sum of a pair equals the target, return their indices.
#
# Time Complexity: O(n²)
# Space Complexity: O(1)
class Solution:
  def twoSum(self,nums,target):
    for i in range(len(nums)):
      for j in range(i+1,len(nums)):
         if nums[i]+nums[j]==target:
            return  [i,j]
