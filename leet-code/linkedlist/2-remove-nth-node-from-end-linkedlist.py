# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head 
        for _ in range(n) :
            fast = fast.next 

        if not fast :               # if only single node in linkedlist
            return head.next

        while fast.next :           # get n th node from end
            slow,fast = slow.next,fast.next

        slow.next = slow.next.next  # remove the element
    
        return head