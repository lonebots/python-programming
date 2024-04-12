''''
question : 
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9

''''


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