''' 
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

Example 1:

Input: root = [4,2,6,1,3]
Output: 1

Example 2:

Input: root = [1,0,48,null,null,12,49]
Output: 1
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nodeValues = []

        def dfs(root) :
            # base case
            if not root :
                return 
            nodeValues.append(root.val)
            dfs(root.left)
            dfs(root.right)

        dfs(root)    

        nodeValues.sort()
        minDiff = 1e9
        for i in range(1,len(nodeValues)) :
            minDiff = min(minDiff, nodeValues[i] - nodeValues[i-1])
        return minDiff
