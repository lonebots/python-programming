'''
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

Example 1:

Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right :
            return head 

        dummyHead = ListNode(0,head)
        prev = dummyHead 

        for i in range(left-1) :
            prev = prev.next

        curr = prev.next
        reverse = None 
        for i in range(right-left+1) :
            next = curr.next
            curr.next = reverse
            reverse = curr
            curr = next 
        
        prev.next.next = curr
        prev.next = reverse

        return dummyHead.next