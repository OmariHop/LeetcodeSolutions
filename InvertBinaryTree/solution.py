# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        if root == None:
            return
        
        self.invertTree(root.left)
        self.invertTree(root.right)

     
        temp = root.right
        root.right = root.left
        root.left =  temp
            
        
        return root
        
            
            
