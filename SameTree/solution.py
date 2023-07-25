# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right+

class Solution(object):
    def isSameTree(self, p, q):

        # Checks if both p and q are NULL, if so we return True indicating both nodes are equal
        if p is None and q is None:
            return True
        # Checks if one or the other is None, it does not matter which one is as long as their is one node that is NULL we return False, indicating that the trees are not equal
        if p is None or q is None:
            return False

        # Once we verify that both nodes exist, we check to see if both nodes have the same value
        # If so we return True, else we return False indicating an imbalane
        if p.val != q.val:
            return False
        # storing the left and right outputs of our current node
        leftBool = self.isSameTree(p.left, q.left)
        rightBool = self.isSameTree(p.right, q.right)

        # if we find that both left and right child nodes returned true, we know that at that point are tree is balanced
        if leftBool == True and rightBool == True:
            return True
        # Return False if otherwise
        return False

        
