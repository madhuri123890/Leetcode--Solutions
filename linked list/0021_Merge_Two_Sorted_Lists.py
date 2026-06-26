# Problem: 21. Merge Two Sorted Lists
#
# Approach:
# - Traverse both linked lists and store all values in an array.
# - Sort the array.
# - Create a new linked list from the sorted values.
# - Return the head of the new merged linked list.
#
# Time Complexity: O((m + n) log(m + n))
# - Collecting values takes O(m + n).
# - Sorting the array takes O((m + n) log(m + n)).
# - Building the new linked list takes O(m + n).
#
# Space Complexity: O(m + n)
# - An extra array is used to store all node values.

class Solution:
    def mergeTwoLists(self, list1, list2):
        arr = []

        while list1:
            arr.append(list1.val)
            list1 = list1.next

        while list2:
            arr.append(list2.val)
            list2 = list2.next

        arr.sort()

        if not arr:
            return None

        head = ListNode(arr[0])
        temp = head

        for x in arr[1:]:
            temp.next = ListNode(x)
            temp = temp.next

        return head
