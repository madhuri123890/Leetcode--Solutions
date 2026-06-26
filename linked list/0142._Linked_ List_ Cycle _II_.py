# Problem: 142. Linked List Cycle II
#
# Approach:
# - Traverse the linked list node by node.
# - Store each visited node in a list.
# - If the current node is already in the visited list,
#   return that node as the start of the cycle.
# - If the end of the list is reached, return None.
#
# Time Complexity: O(n²)
# - Checking `head in visited` takes O(n) time for each node.
#
# Space Complexity: O(n)
# - The visited list stores all traversed nodes.

class Solution:
    def detectCycle(self, head):
        visited = []

        while head:
            visited.append(head)
            head = head.next

            if head in visited:
                return head

        return None
