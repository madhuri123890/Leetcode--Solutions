# Problem: 206. Reverse Linked List
# Approach:
# - Use two pointers: prev and curr.
# - Traverse the linked list one node at a time.
# - Reverse the current node's next pointer to point to the previous node.
# - Move both pointers forward until the end of the list.
# - Return prev, which becomes the new head of the reversed list.
#
# Time Complexity: O(n)
# - Each node is visited exactly once.
#
# Space Complexity: O(1)
# - Only a few pointer variables are used.

class Solution:
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev
