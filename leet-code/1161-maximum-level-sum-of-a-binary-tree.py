''' 
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

 

Example 1:

Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.

'''

 # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        max_val_level = 0
        max_sum = float('-inf')
        level = 0

        # do a bfs 
        q = [root] 

        while q :
            level += 1 
            curr_sum = 0

            for _ in range(len(q)) :
                node = q.pop(0)
                curr_sum += node.val

                if node.left :
                    q.append(node.left)
                if node.right :
                    q.append(node.right)

            if max_sum < curr_sum :
                max_sum, max_val_level = curr_sum, level
        return max_val_level
        
