class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        # approach 1 : brute force --> TLE
        # maxDist = 0
        # for i in range(len(nums1)) :
        #     for j in range(i, len(nums2)) :
        #         if nums1[i] <= nums2[j] :
        #             maxDist = max(maxDist, j -i)

        # return maxDist

        # approach 2 : 
        i = j = 0 # for traversing nums1 and nums2 respectivly

        maxDist = 0 
        while i < len(nums1) and j < len(nums2) : # take of the search space
            # check for the condition nums1[i] <= nums2[j]
            if nums1[i] <= nums2[j] :
                maxDist = max(maxDist,j -i ) 
                j += 1
            else :
                i += 1

        return maxDist