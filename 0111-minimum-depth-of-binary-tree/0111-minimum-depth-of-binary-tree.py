# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # if not root then return 0
        if not root:
            return 0

        # make a queue, put node and its current depth in it 
        queue = deque([(root,1)])

        # run a loop until no node in the queue
        while queue:

        # take current node and depth from the queue
            current_node, current_depth = queue.popleft()

        # check if this node have not left and right node then it will be a leaf node and our answer
            if not current_node.left and not current_node.right:
                return current_depth

         # check if this node have a left child or a right child then put it in the queue 
            if current_node.left:
                queue.append((current_node.left, current_depth + 1))
            if current_node.right:
                queue.append((current_node.right, current_depth + 1))