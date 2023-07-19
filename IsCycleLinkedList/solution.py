# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):

        # Sets slow and fast to the same reference
        slow = head
        fast = head
        

        # Allows us to see and reference atleast 2 nodes to avoid any reference errors
        # Loops untill our slow and fast pointer meets. If the fast pointer hits NULL we dont have a list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        # Returns false if we do encounter NULL, covers the one node case as well
        return False

        """
        :type head: ListNode
        :rtype: bool
        """
