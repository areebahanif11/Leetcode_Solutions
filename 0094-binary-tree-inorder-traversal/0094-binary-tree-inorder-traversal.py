# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = [] # Initialize the result list once
        self._inorder_helper(root, result) # Call the helper function
        return result

    # Private helper function to perform the recursive traversal
    def _inorder_helper(self, node: Optional[TreeNode], result: List[int]):
        if not node: # Base case: if node is null, do nothing
            return

        self._inorder_helper(node.left, result)  # Traverse left
        result.append(node.val)                 # Visit current node
        self._inorder_helper(node.right, result) # Traverse right


        