# Problem: 138. Copy List with Random Pointer
#
# Approach:
# - Traverse the linked list and create a copy of each node.
# - Store the mapping from original node to copied node in a dictionary.
# - Traverse the list again to connect the next and random pointers.
# - Return the head of the copied linked list.
#
# Time Complexity: O(n)
# - The linked list is traversed twice.
#
# Space Complexity: O(n)
# - A dictionary is used to store the mapping of original nodes to copied nodes.

class Solution:
    def copyRandomList(self, head):
        if not head:
            return None

        d = {}
        temp = head

        while temp:
            d[temp] = Node(temp.val)
            temp = temp.next

        temp = head

        while temp:
            d[temp].next = d.get(temp.next)
            d[temp].random = d.get(temp.random)
            temp = temp.next

        return d[head]
