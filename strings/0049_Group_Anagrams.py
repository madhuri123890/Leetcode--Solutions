# Problem: 49. Group Anagrams
#
# Approach:
# - Traverse each word in the list.
# - Sort the characters of the word to create a key.
# - Use a dictionary to group words with the same sorted key.
# - Return all the grouped anagrams.
#
# Time Complexity: O(n × k log k)
# - n = number of strings
# - k = maximum length of a string
# - Sorting each string takes O(k log k).
#
# Space Complexity: O(n × k)
# - The dictionary stores all input strings.

class Solution:
    def groupAnagrams(self, strs):
        result = {}

        for word in strs:
            key = "".join(sorted(word))

            if key in result:
                result[key].append(word)
            else:
                result[key] = [word]

        return list(result.values())
