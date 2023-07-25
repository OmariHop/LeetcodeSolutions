# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
      # Returning a depth of 0 if we are at a NULL node
        if root == None:
            return 0

        # Getting the left and right heights of a node recursively before returning the hight of our current node 
        # The height of our current node would be the max of the two nodes + 1 since a node is counted as 1
        leftSum = self.maxDepth(root.left)
        rightSum = self.maxDepth(root.right)

        return max(leftSum, rightSum) + 1
