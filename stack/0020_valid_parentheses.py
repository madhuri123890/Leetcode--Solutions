# Problem: 20. Valid Parentheses
#
# Approach:
# - Use a stack to store the expected closing brackets.
# - For every opening bracket, push its matching closing bracket.
# - For every closing bracket, check if it matches the top of the stack.
# - If it doesn't match or the stack is empty, return False.
# - At the end, return True if the stack is empty.
#
# Time Complexity: O(n)
# - Traverse the string once.
#
# Space Complexity: O(n)
# - The stack may store all opening brackets.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch == "(":
                stack.append(")")
            elif ch == "{":
                stack.append("}")
            elif ch == "[":
                stack.append("]")
            else:
                if stack == []:
                    return False
                if ch != stack.pop():
                    return False

        return stack == []
