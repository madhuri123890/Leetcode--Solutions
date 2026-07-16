# Problem: 155. Min Stack
#
# Approach:
# - Use a list as a stack.
# - Push elements onto the stack.
# - Pop the top element when required.
# - Return the top element using the last index.
# - Find the minimum element using min().
#
# Time Complexity:
# - push(): O(1)
# - pop(): O(1)
# - top(): O(1)
# - getMin(): O(n)
#   - min() scans the entire stack.
#
# Space Complexity: O(n)
# - The stack stores all inserted elements.

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return min(self.stack)
