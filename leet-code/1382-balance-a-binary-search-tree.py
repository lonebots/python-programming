'''
Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

 

Example 1:

Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.

Example 2:

Input: root = [2,1,3]
Output: [2,1,3]

 

Constraints:

    The number of nodes in the tree is in the range [1, 104].
    1 <= Node.val <= 105

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        inorder = []
        self.inorder_traversal(root, inorder)

        return self.create_balanced_bst(inorder, 0, len(inorder) - 1)

        
    def inorder_traversal(self, root: TreeNode, inorder: List):
        if not root :
            return 

        self.inorder_traversal(root.left, inorder)
        inorder.append(root.val)
        self.inorder_traversal(root.right, inorder)

    def create_balanced_bst(self, inorder: List, start: int, end: int) -> TreeNode:
        if start > end :
            return None 

        mid = start + (end - start) // 2 

        left_subtree = self.create_balanced_bst(inorder, start, mid - 1)
        right_subtree = self.create_balanced_bst(inorder, mid + 1, end) 

        node = TreeNode(inorder[mid], left_subtree, right_subtree) 
        return node 