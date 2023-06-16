'''
Given an array nums that represents a permutation of integers from 1 to n. We are going to construct a binary search tree (BST) by inserting the elements of nums in order into an initially empty BST. Find the number of different ways to reorder nums so that the constructed BST is identical to that formed from the original array nums.

For example, given nums = [2,1,3], we will have 2 as the root, 1 as a left child, and 3 as a right child. The array [2,3,1] also yields the same BST but [3,2,1] yields a different BST.
Return the number of ways to reorder nums such that the BST formed is identical to the original BST formed from nums.

Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:


Input: nums = [2,1,3]
Output: 1
Explanation: We can reorder nums to be [2,3,1] which will yield the same BST. There are no other ways to reorder nums which will yield the same BST. 
'''

import math
class Solution(object):
    def numOfWays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mod = 10 ** 9 + 7 

        # dfs to computer the total combinations possible 
        '''
        dfs(nums) = p * dfs(left_node) * dfs(right_nodes)
        p --> permutations possible with same relative order 
        '''
        def dfs (nums) :
            m = len(nums)
            
            # base case 
            if m < 3 : 
                return 1 

            # other case 
            left_nodes = [node for node in nums if node < nums[0]]
            right_nodes = [node for node in nums if node > nums[0]]
            return dfs(left_nodes) * dfs(right_nodes) * math.comb(len(left_nodes) + len(right_nodes), len(right_nodes))
            

        
        return (dfs(nums) - 1)% mod