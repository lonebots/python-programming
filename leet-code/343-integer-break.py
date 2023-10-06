'''
Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

Return the maximum product you can get.

 

Example 1:

Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.

Example 2:

Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.

 

Constraints:

    2 <= n <= 58

'''

class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {1:1} 
        def dfs (num) :
            if num in dp :
                return dp[num]
            
            dp[num] = 0 if num == n else num 
            for i in range(1,num ) :
                val = dfs(i) * dfs(num - i) 
                dp[num] = max(dp[num],val)
            return dp[num]
        return dfs(n)