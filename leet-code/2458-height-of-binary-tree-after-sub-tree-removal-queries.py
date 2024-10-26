'''
You are given the root of a binary tree with n nodes. Each node is assigned a unique value from 1 to n. You are also given an array queries of size m.

You have to perform m independent queries on the tree where in the ith query you do the following:

    Remove the subtree rooted at the node with the value queries[i] from the tree. It is guaranteed that queries[i] will not be equal to the value of the root.

Return an array answer of size m where answer[i] is the height of the tree after performing the ith query.

Note:

    The queries are independent, so the tree returns to its initial state after each query.
    The height of a tree is the number of edges in the longest simple path from the root to some node in the tree.

 

Example 1:

Input: root = [1,3,4,2,null,6,5,null,null,null,null,null,7], queries = [4]
Output: [2]
Explanation: The diagram above shows the tree after removing the subtree rooted at node with value 4.
The height of the tree is 2 (The path 1 -> 3 -> 2).

Example 2:

Input: root = [5,8,9,2,1,3,7,4,6], queries = [3,2,4,8]
Output: [3,2,3,2]
Explanation: We have the following queries:
- Removing the subtree rooted at node with value 3. The height of the tree becomes 3 (The path 5 -> 8 -> 2 -> 4).
- Removing the subtree rooted at node with value 2. The height of the tree becomes 2 (The path 5 -> 8 -> 1).
- Removing the subtree rooted at node with value 4. The height of the tree becomes 3 (The path 5 -> 8 -> 2 -> 6).
- Removing the subtree rooted at node with value 8. The height of the tree becomes 2 (The path 5 -> 9 -> 3).

 

Constraints:

    The number of nodes in the tree is n.
    2 <= n <= 105
    1 <= Node.val <= n
    All the values in the tree are unique.
    m == queries.length
    1 <= m <= min(n, 104)
    1 <= queries[i] <= n
    queries[i] != root.val

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        max_height_after_removal = [0] * 100001  # keep track of all max height for each query
        self.curr_max_height = 0                 # for storing the max height at present

        def _traverse_left_to_right(node, curr_height):
            if not node:
                return 

            # store the current height as if removing the subtree
            max_height_after_removal[node.val] = self.curr_max_height

            # update current maximum height
            self.curr_max_height = max(curr_height, self.curr_max_height)

            # traverse along left and right sub tree
            _traverse_left_to_right(node.left, curr_height + 1)
            _traverse_left_to_right(node.right, curr_height + 1)

        
        def _traverse_right_to_left(node, curr_height):
            if not node:
                return
            
            max_height_after_removal[node.val] = max(self.curr_max_height, max_height_after_removal[node.val])

            self.curr_max_height = max(self.curr_max_height, curr_height)

            # traverse in reverse pre order => (root, right, left)
            _traverse_right_to_left(node.right, curr_height + 1)
            _traverse_right_to_left(node.left, curr_height + 1)

        
        _traverse_left_to_right(root, 0)
        self.curr_max_height = 0 # reset for second traversal
        _traverse_right_to_left(root, 0)

        # process and return the query result in a array
        return [max_height_after_removal[q] for q in queries]