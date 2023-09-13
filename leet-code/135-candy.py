'''
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

 

Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
'''

class Solution:
    def candy(self, ratings: List[int]) -> int:
      n = len(ratings)
      candies = [1] * n 

      # first pass 
      for i in range(1,n) :
        if ratings[i-1] < ratings[i] and candies[i-1] >= candies[i] :
          candies[i] = candies[i-1] + 1

      # second pass
      for i in range(n-2,-1,-1) :
        if ratings[i+1] < ratings[i] and candies[i+1] >= candies[i] :
          candies[i] = candies[i+1] + 1

      total_candies = sum(candies)

      return total_candies