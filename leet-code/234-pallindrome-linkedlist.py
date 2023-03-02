# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head 
        prev = None

        while fast and fast.next :
            slow, fast = slow.next, fast.next.next
        
        while slow :
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next 
            
        left ,right = head, prev
        while right :
            if left.val != right.val :
                return False 
            left, right = left.next, right.next
        return True