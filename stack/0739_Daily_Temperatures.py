# Problem: 739. Daily Temperatures
#
# Approach:
# - Use a stack to store the indices of temperatures.
# - Traverse the temperatures array.
# - When the current temperature is higher than the temperature
#   at the top index of the stack, calculate the number of days
#   and store it in the answer array.
# - Push the current index onto the stack.
# - Return the answer array.
#
# Time Complexity: O(n)
# - Each index is pushed and popped from the stack at most once.
#
# Space Complexity: O(n)
# - The stack and answer array use extra space.

class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        ans = [0] * n
        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                ans[prev] = i - prev

            stack.append(i)

        return ans
