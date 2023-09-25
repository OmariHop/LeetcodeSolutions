# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False


        def dfs(root, currSum):
            if root == None:
                return False
            # meaning we are at a leaf node
            if not root.right and not root.left:
                if root.val + currSum == targetSum:
                    return True
                else:
                    return False
            
            leftBool = dfs(root.left, currSum + root.val)
            rightBool = dfs(root.right, currSum + root.val)


            if leftBool or rightBool:
                return True
            else:
                return False

        return dfs(root, 0)
                
        
