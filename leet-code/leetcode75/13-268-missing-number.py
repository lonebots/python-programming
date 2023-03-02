# easy question 
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # n = len(nums) 
        # return n*(n+1)//2 - sum(nums)


        # approach 2 
        res = len(nums)
        for i in range(len(nums)) :
            res += (i - nums[i])

        return res