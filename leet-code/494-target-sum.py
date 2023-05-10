"""
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

    For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".

Return the number of different expressions that you can build, which evaluates to target.

 

Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

Example 2:

Input: nums = [1], target = 1
Output: 1

"""


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Calculate the sum of all elements in the input list
        summ = sum(nums)
        # If the target is greater than the sum of all elements or their absolute difference is odd,
        # there's no way to form the target sum by adding or subtracting elements from the input list.
        if summ < abs(target) or (summ + target) & 1:
            return 0

        def knapsack(target: int) -> int:
            # Create a list with a length equal to the sum of all elements in the input list plus one,
            # where the first element is initialized to 1 and the rest are initialized to 0.
            # This list will be used to keep track of the number of ways to sum up to each possible target.
            dp = [1] + [0] * summ

            # For each element in the input list,
            for num in nums:
                # Iterate backwards through the dp list from the end to the current element (inclusive),
                # so that the dp values for the current element are only based on the previous elements
                # in the list, and not the current element or any elements after it.
                for j in range(summ, num - 1, -1):
                    # Add the dp value for the previous element at the current index, j - num,
                    # to the dp value for the current index, j.
                    # This is because there are dp[j - num] ways to sum up to the target using all elements
                    # up to and including the current element, and we're adding those ways to the existing ways
                    # to sum up to the target using all elements up to but not including the current element.
                    dp[j] += dp[j - num]

            # Return the dp value for the target sum.
            return dp[target]

        # Call the knapsack function with the target sum divided by 2, because we're counting the number
        # of ways to form the target sum using addition and subtraction, and the two operations can cancel
        # each other out, meaning that the target sum can only be achieved if it's an even number.
        return knapsack((summ + target) // 2)
