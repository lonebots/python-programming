'''
1. here left and right pointers are used to solve 
2. maxL and maxR points to the maximum neighbouring heights of the current block under consideration (based on left or right you consider)
3. water variable stores the final result which add up the water units while the traversal happens
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height : return 0

        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        water = 0 
        while l < r :

            if maxL < maxR :
                l += 1
                maxL = max(maxL, height[l])
                water +=  maxL - height[l]
            else :
                r -= 1
                maxR = max(maxR, height[r])
                water += maxR - height[r]
        return water