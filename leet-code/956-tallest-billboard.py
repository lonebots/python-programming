'''
You are installing a billboard and want it to have the largest height. The billboard will have two steel supports, one on each side. Each steel support must be an equal height.

You are given a collection of rods that can be welded together. For example, if you have rods of lengths 1, 2, and 3, you can weld them together to make a support of length 6.

Return the largest possible height of your billboard installation. If you cannot support the billboard, return 0.

 

Example 1:

Input: rods = [1,2,3,6]
Output: 6
Explanation: We have two disjoint subsets {1,2,3} and {6}, which have the same sum = 6.
Example 2:

Input: rods = [1,2,3,4,5,6]
Output: 10
Explanation: We have two disjoint subsets {2,3,5} and {4,6}, which have the same sum = 10.
Example 3:

Input: rods = [1,2]
Output: 0
Explanation: The billboard cannot be supported, so we return 0.
'''

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:

        # meet in the middle approach 
        def helper(half_rods) :
            states = set() # to store the state values 
            states.add((0,0))

            for r in half_rods : 
                new_states = set()
                for left, right in states :
                    new_states.add((left+r, right))
                    new_states.add((left, right+r))
                states |= new_states

            dp ={}
            for left,right in states :
                dp[left-right] = max(dp.get(left-right,0),left)
            return dp

        n = len(rods)
        first_half = helper(rods[:n//2])
        second_half = helper(rods[n//2:])

        answer = 0
        for diff in first_half :
            if -diff in second_half :
                answer = max(answer, first_half[diff] + second_half[-diff])
        return answer