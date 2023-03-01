class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # dynamic programming
        res = max(nums) 
        currMin, currMax = 1, 1 

        for n in nums :
            if n == 0 :
                currMin, currMax = 1, 1
                continue
            
            tmp = n * currMax
            currMax = max(n, n * currMax, n * currMin)
            currMin = min(n, n * currMin, tmp)

            res= max(currMax,res)

        return res