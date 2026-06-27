# Problem: 143. Reorder List
#
# Approach:
# - Store all linked list nodes in an array.
# - Use two pointers (i and j) from the beginning and end.
# - Connect nodes alternately from the front and back.
# - Continue until the pointers meet.
# - Set the last node's next pointer to None.
#
# Time Complexity: O(n)
# - Traverse the linked list once and reorder the nodes.
#
# Space Complexity: O(n)
# - An extra array is used to store all the nodes.

class Solution:
    def reorderList(self, head):
        arr = []

        while head:
            arr.append(head)
            head = head.next

        i = 0
        j = len(arr) - 1

        while i < j:
            arr[i].next = arr[j]
            i += 1

            arr[j].next = arr[i]
            j -= 1

        arr[i].next = None
