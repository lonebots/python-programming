class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        '''Wrong answer '''
        result = [-1] * len(nums)
        stack = []
        map_ = {}
        for i in range(len(nums)) :
            while stack and nums[i] > nums[stack[-1]] :
                result[stack.pop()] = nums[i]
            stack.append(i)
        for i in range(len(nums)) :
            while stack and nums[i] > nums[stack[-1]] :
                result[stack.pop()] = nums[i]
            stack.append(i)

        return result