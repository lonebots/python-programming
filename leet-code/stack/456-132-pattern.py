'''
Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.

 

Example 1:

Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.

Example 2:

Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

Example 3:

Input: nums = [-1,3,2,0]
Output: true
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].

 

Constraints:

    n == nums.length
    1 <= n <= 2 * 105
    -109 <= nums[i] <= 109

'''

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = [] # pair : (num, minLeft)
        currMin = nums[0]

        for n in nums[1:] :
            while stack and stack[-1][0] <= n : # monotonically decreasing
                stack.pop()

            # two cases : 
            # 1. stack is available then check if n > minLeft : then True (132) is occured
            # 2. stack is empty so --> append the (n,currMin) , update currMin = min(currMin,n) 

            # case 1
            if stack and n > stack[-1][1] :
                return True

            # case 2
            stack.append((n,currMin)) 
            currMin = min(currMin, n)

        return False

# failed attempt 
        # stack  = []

        # for n in nums :
        #     while stack and stack[-1] < n :
        #         if len(stack) >= 2 :
        #             return True  
        #         else :
        #             stack.pop()  
        #     stack.append(n)
            
        # return False