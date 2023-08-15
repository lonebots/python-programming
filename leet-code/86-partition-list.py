'''
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

 

Example 1:


Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:

Input: head = [2,1], x = 2
Output: [1,2]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # create two basket 1. before, 2. after 
        # add the nodes accordingly 
        # merge the list finally

        before, after = ListNode(0), ListNode(0)
        
        # keep their curr pointer
        before_curr, after_curr = before, after

        while head : 
            if head.val < x :
                before_curr.next, before_curr = head,head
            else :
                after_curr.next, after_curr = head,head
            head = head.next

        # point end of after to none
        after_curr.next = None 
        
        # connect before to start of after 
        before_curr.next = after.next

        return before.next