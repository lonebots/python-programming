class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0 :
            return [-1,-1]
        
        l,r = 0,len(nums) -1
        while l <= r :
            if nums[l] == target and nums[r] == target :
                return [l,r]
            elif nums[l] < target :
                l += 1
            elif nums[r] > target :
                r -= 1
        return [-1,-1]