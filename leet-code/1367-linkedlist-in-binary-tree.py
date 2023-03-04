class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        @lru_cache(None)
        def check(node, cur=head):
            if not cur: return True
            if not node: return False
            return check(node.left, head) or check(node.right, head) or \
        node.val == cur.val and (check(node.left, cur.next) or check(node.right, cur.next))
        
        return check(root, head)