# Problem: 876. Middle of the Linked List
#
# Approach:
# - Traverse the linked list and store each node in a list.
# - Find the middle index using len(arr) // 2.
# - Return the node at the middle index.
#
# Time Complexity: O(n)
# - We traverse the linked list once.
#
# Space Complexity: O(n)
# - Extra space is used to store all nodes in the list.

class Solution:
    def middleNode(self, head):
        arr = []

        while head:
            arr.append(head)
            head = head.next

        middle = len(arr) // 2
        return arr[middle]
