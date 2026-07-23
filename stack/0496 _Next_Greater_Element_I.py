# Problem: 496. Next Greater Element I
#
# Approach:
# - Use a stack to keep track of elements whose next greater
#   element has not been found.
# - Traverse nums2.
# - When the current number is greater than the top of the stack,
#   it is the next greater element for that stack element.
# - Store the mapping in a dictionary.
# - For remaining elements in the stack, store -1.
# - Build the answer for nums1 using the dictionary.
#
# Time Complexity: O(n + m)
# - n = length of nums2, m = length of nums1.
# - Each element is pushed and popped from the stack at most once.
#
# Space Complexity: O(n)
# - The stack and dictionary store elements from nums2.

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        d = {}

        for num in nums2:
            while stack and num > stack[-1]:
                prev = stack.pop()
                d[prev] = num

            stack.append(num)

        while stack:
            d[stack.pop()] = -1

        ans = []

        for num in nums1:
            ans.append(d[num])

        return ans
