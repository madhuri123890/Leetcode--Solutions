# Problem: 150. Evaluate Reverse Polish Notation
#
# Approach:
# - Use a stack to store numbers.
# - Traverse each token.
# - If the token is an operator, pop the top two numbers,
#   perform the operation, and push the result back.
# - If the token is a number, push it onto the stack.
# - Return the final value from the stack.
#
# Time Complexity: O(n)
# - Each token is processed once.
#
# Space Complexity: O(n)
# - The stack stores numbers during evaluation.

class Solution:
    def evalRPN(self, tokens):
        stack = []

        for ch in tokens:
            if ch == '+':
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)

            elif ch == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)

            elif ch == '*':
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)

            elif ch == '/':
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a / b))

            else:
                stack.append(int(ch))

        return stack.pop()
