# Problem: 19. Remove Nth Node From End of List
#
# Approach:
# - Traverse the linked list and store all nodes in a list.
# - Find the index of the node to remove using:
#   remove = len(arr) - n
# - If the first node needs to be removed, return head.next.
# - Otherwise, link the previous node to the next node of the
#   node being removed.
# - Return the modified linked list.
#
# Time Complexity: O(n)
# - The linked list is traversed once.
#
# Space Complexity: O(n)
# - An extra list is used to store all the nodes.

class Solution:
    def removeNthFromEnd(self, head, n):
        arr = []
        temp = head

        while temp:
            arr.append(temp)
            temp = temp.next

        remove = len(arr) - n

        if remove == 0:
            return head.next

        arr[remove - 1].next = arr[remove].next
        return head
