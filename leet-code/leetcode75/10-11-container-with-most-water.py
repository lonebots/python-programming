class Solution:
    def maxArea(self, height: List[int]) -> int:
        # brute force  - TLE
        # maxarea = 0
        # for i in range(len(height)) :
        #     for j in range(i+1, len(height)) :
        #         width = j - i 
        #         maxarea = max(maxarea, width * min(height[i],height[j]))

        # return maxarea

        maxarea = 0 
        left = 0
        right = len(height) - 1

        while left < right : 
            width = right - left 
            maxarea = max(maxarea, width * min(height[left],height[right]))

            if height[left] <= height[right] :
                left += 1 
            else :
                right -= 1 

        return maxarea