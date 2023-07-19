# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        # Creates the node object for the linked list
        head = ListNode()
        # Setting tail to the head for easier traversal
        tail = head

        # Loops for as long as list 1 and list 2 exist 
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                 tail.next = list2
                 list2 = list2.next
            # List traversal at the end of the if conditions
            tail = tail.next

        # Once one of the list hit void, we check to see if either or end, and append it to the rest of the next
        if list2:
                tail.next = list2

        if list1:
                tail.next = list1
    

        return head.next

            

        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
