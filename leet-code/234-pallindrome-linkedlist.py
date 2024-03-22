'''
Given the head of a singly linked list, return true if it is a
palindrome
or false otherwise.

Example 1:

Input: head = [1,2,2,1]
Output: true

Example 2:

Input: head = [1,2]
Output: false

Constraints:

    The number of nodes in the list is in the range [1, 105].
    0 <= Node.val <= 9

Follow up: Could you do it in O(n) time and O(1) space?
'''

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