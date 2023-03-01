class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i, num in enumerate(nums) :
            if i > 0 and num == nums[i-1] :
                continue
            
            l , r = i + 1, len(nums) -1 
            while l < r : 
                sum  = num + nums[l] + nums[r] 
                if sum == 0 :
                    result.append([num , nums[l] , nums[r]])
                    l += 1 
                    while nums[l] == nums[l-1] and l < r :
                        l += 1
                if sum < 0 :
                    l += 1 
                    
                else :
                    r -= 1
        return result