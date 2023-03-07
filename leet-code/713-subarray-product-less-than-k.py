class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # brute force 
        # count = 0
        # for i in range(len(nums)) :
        #     for j in range(i, len(nums)) :
        #         prod  = 1
        #         for l in range(i,j+1) :
        #             prod *= nums[l]   
        #         if prod < k :
        #             count += 1
        # return count

        # two pointers sliding window
        if k <= 1 :
            return 0
        result = 0 
        right = left = 0
        prod = 1
        while right < len(nums) :
            prod *= nums[right] 
            while prod >= k :
                prod //= nums[left]
                left += 1
            
            result += right - left + 1
            right += 1
        
        return result