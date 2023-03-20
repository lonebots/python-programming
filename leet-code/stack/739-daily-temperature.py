'''
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]

'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # approach 1 : brute force 
        # for i in range(len(temperatures)) :
        #     tmp = temperatures[i]
        #     for j in range(i + 1, len(temperatures)) :
        #         if temperatures[j] > temperatures[i] :
        #             temperatures[i] = j - i 
        #             break
        #     if temperatures[i] == tmp :
        #         temperatures[i] = 0 
        # return temperatures

        stack = []
        wait = [0] * len(temperatures) 

        for curr_day,curr_temp in enumerate(temperatures) :
            while stack and temperatures[stack[-1]] < curr_temp :
                prev_day = stack.pop()
                wait[prev_day] = curr_day - prev_day

            stack.append(curr_day)

        return wait