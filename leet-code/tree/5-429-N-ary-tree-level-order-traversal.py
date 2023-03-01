"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root : return []
        q = [root]
        res = []
        while q :
            level = []
            for _ in range(len(q)) :
                node = q.pop(0)
                level.append(node.val)
                for child in node.children :
                    q.append(child)
            res.append(level)
        return res
