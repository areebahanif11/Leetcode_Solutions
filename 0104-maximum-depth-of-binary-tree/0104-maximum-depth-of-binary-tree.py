# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: an empty tree has a depth of 0
        if not root:
            return 0
        
        # Use a stack to store tuples of (node, depth)
        # We start with the root node, and its depth is 1.
        stack = [(root, 1)] 
        
        # This variable will store the maximum depth found so far.
        max_depth = 0
        
        # Continue as long as there are nodes in our stack to visit.
        while stack:
            # Pop the current node and its associated depth from the top of the stack.
            # DFS explores "deepest" nodes first because of LIFO (Last-In, First-Out).
            node, current_depth = stack.pop()
            
            # Update the overall maximum depth found so far.
            # 'current_depth' is the depth of the node we just popped.
            max_depth = max(max_depth, current_depth)
            
            # If the node has a left child, push it onto the stack.
            # Its depth will be one greater than the current node's depth.
            if node.left:
                stack.append((node.left, current_depth + 1))
            
            # If the node has a right child, push it onto the stack.
            # Its depth will also be one greater than the current node's depth.
            # Pushing right then left means left is processed *before* right (due to stack's LIFO).
            # The order of pushing children doesn't change the final max_depth,
            # only the order of traversal.
            if node.right:
                stack.append((node.right, current_depth + 1))
                
        # Once the stack is empty, all reachable nodes have been visited,
        # and max_depth holds the maximum depth of the tree.
        return max_depth


        