# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root :
            return 0
        self.min_depth = float('inf')
        def traverse(root,depth) :
            if root : 
                if not root.right and not root.left :
                    self.min_depth = min(self.min_depth,depth)
                traverse(root.right,depth + 1) 
                traverse(root.left,depth + 1) 
        
        traverse(root,1) 
        return self.min_depth