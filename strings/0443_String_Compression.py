# Problem: 443. String Compression
#
# Approach:
# - Traverse the characters one by one.
# - Count consecutive repeated characters.
# - Add the character to the result string.
# - If the count is greater than 1, append the count.
# - Copy the compressed result back into the original array.
# - Return the length of the compressed string.
#
# Time Complexity: O(n)
# - The characters are traversed once, and copying the result
#   back also takes linear time.
#
# Space Complexity: O(n)
# - An extra string (`result`) is used to build the compressed output.

class Solution:
    def compress(self, chars):
        result = ""
        count = 1

        for i in range(len(chars)):
            if i < len(chars) - 1 and chars[i] == chars[i + 1]:
                count += 1
            else:
                result += chars[i]
                if count > 1:
                    result += str(count)
                count = 1

        for i in range(len(result)):
            chars[i] = result[i]

        return len(result)
