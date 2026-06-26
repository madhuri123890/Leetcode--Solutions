# Problem: 141. Linked List Cycle
#
# Approach:
# - Traverse the linked list node by node.
# - Store each visited node in a list.
# - Before moving to the next node, check if it has already been visited.
# - If a node is visited again, a cycle exists, so return True.
# - If the traversal reaches the end (None), return False.
#
# Time Complexity: O(n²)
# - Checking `head in visited` takes O(n) time for each node.
#
# Space Complexity: O(n)
# - The visited list stores all traversed nodes.

class Solution:
    def hasCycle(self, head):
        visited = []

        while head:
            visited.append(head)
            head = head.next

            if head in visited:
                return True

        return False
