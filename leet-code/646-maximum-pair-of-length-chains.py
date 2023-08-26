''' 
You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.

A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.

Return the length longest chain which can be formed.

You do not need to use up all the given intervals. You can select pairs in any order.

 

Example 1:

Input: pairs = [[1,2],[2,3],[3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4].
Example 2:

Input: pairs = [[1,2],[7,8],[4,5]]
Output: 3
Explanation: The longest chain is [1,2] -> [4,5] -> [7,8].
 

Constraints:

n == pairs.length
1 <= n <= 1000
-1000 <= lefti < righti <= 1000
'''

class Solution:
    def longestPairChain(self,i,pairs,n,memo) :
        if memo[i] != 0:
            return memo[i]

        memo[i] = 1 
        for j in range(i+1,n) :
            if pairs[i][1] < pairs[j][0] :
                memo[i] = max(memo[i],1 + self.longestPairChain(j,pairs,n,memo))
        
        return memo[i]

    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        pairs.sort()
        memo = [0] * n

        ans = 0 
        for i in range(n) :
            ans = max(ans, self.longestPairChain(i,pairs,n,memo))

        return ans        