# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__ (self) :
        self.max_depth = float('-inf')
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def traverse(root, depth) :
            if root :
                traverse(root.left,depth + 1)
                traverse(root.right,depth + 1)
            
            self.max_depth = max(self.max_depth, depth)

        traverse(root,depth = 0)
        
        return self.max_depth

