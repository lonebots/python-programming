"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        travelhistory_ = []

        def traverse (root) :
            if not root :
                return 
            for child in root.children :
                traverse(root.children)
            travelhistory_.append(root.val) 
        
        traverse(root)

        return travelhistory_