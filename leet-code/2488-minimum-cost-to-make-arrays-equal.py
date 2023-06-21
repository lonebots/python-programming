'''
You are given two 0-indexed arrays nums and cost consisting each of n positive integers.

You can do the following operation any number of times:

Increase or decrease any element of the array nums by 1.
The cost of doing one operation on the ith element is cost[i].

Return the minimum total cost such that all the elements of the array nums become equal.

 

Example 1:

Input: nums = [1,3,5,2], cost = [2,3,1,14]
Output: 8
Explanation: We can make all the elements equal to 2 in the following way:
- Increase the 0th element one time. The cost is 2.
- Decrease the 1st element one time. The cost is 3.
- Decrease the 2nd element three times. The cost is 1 + 1 + 1 = 3.
The total cost is 2 + 3 + 3 = 8.
It can be shown that we cannot make the array equal with a smaller cost.
Example 2:

Input: nums = [2,2,2,2,2], cost = [4,2,8,1,3]
Output: 0
Explanation: All the elements are already equal, so no operations are needed.
'''

class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        
        # # do the nums -> cost mapping
        # costmap = {}
        # target_cost = max(cost)
        # target_num = 0
        # for index in range(len(nums)) :
        #     if cost[index] == target_cost :
        #         target_num = nums[index]
        #     costmap[nums[index]] = cost[index]

        # result = 0
        # for n in nums : 
        #     result += abs(n-target_num) * costmap[n]
        
        # return result

        # sorted value 
        costmap = sorted([num,c] for num,c in zip(nums,cost))
        n = len(nums)

        # prefix
        prefix_cost = [0] * n
        prefix_cost[0] = costmap[0][1]

        # initialize the prefix cost values ( running sum)
        for i in range(1,n) :
            prefix_cost[i] = costmap[i][1] + prefix_cost[i-1]

        # make every nums[i] to target nums[i]
        total_cost = 0 
        for i in range(1,n) :
            total_cost += costmap[i][1] * (costmap[i][0] - costmap[0][0])

        result = total_cost 

        # then try every nums[1], nums[2] and so on, the cost difference is made by the change of 
        # two parts : 1. preifx and 2. suffix sum of costs
        # during this iteration, record the minimum cost we have met
        for i in range(1,n) : 
            gap = costmap[i][0] - costmap[i-1][0]
            total_cost += prefix_cost[i-1] * gap
            total_cost -= gap * ( prefix_cost[n-1] - prefix_cost[i-1]) 
            result = min(result, total_cost)
        
        return result