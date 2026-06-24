# Problem: 238. Product of Array Except Self
#
# Approach:
# - For each index i, compute product of all elements except nums[i].
# - Use two nested loops:
#   - Outer loop picks each element as "excluded index"
#   - Inner loop multiplies all other elements
# - Store each result in a list and return it.
#
# Time Complexity: O(n²)
# - For each element, we loop through the array again.
#
# Space Complexity: O(n)
# - Output array is used to store results.

class Solution:
    def productExceptSelf(self, nums):
        answer = []

        for i in range(len(nums)):
            product = 1

            for j in range(len(nums)):
                if i != j:
                    product = product * nums[j]

            answer.append(product)

        return answer
