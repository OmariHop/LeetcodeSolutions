# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Result array that holds each list to be outputted from our different levels   
        res = []
        # Initializing our queue and adding our root node to the queue
        # Queue holds the actual nodes, result holds a list of lists
        q = deque()
        q.append(root)


        # Looping untill our queue is empty
        # Every iteration of our queue represents the different level  or "depth" we are on
        while q:
            # Level list that holds the amount of nodes at a specific level
            level = []
            # We grab the length of our queue in order to control the number of iterations of our for loop
            qLen = len(q)

            # The for loop iterates for each node at a given level\
            # If we are at the second level, this for loop only processes two nodes
            for i in range(qLen):
                # removing the first node in our queue in order to check the validity of that node
                 node = q.popleft()
                 # Once we verify the existence of a node, we add it to our level list, and enqueue its children
                 if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            # Checks to see if our list had any values added to it
            # If it did, we add our level list into our res list 
            if level:
                res.append(level)

        return res

