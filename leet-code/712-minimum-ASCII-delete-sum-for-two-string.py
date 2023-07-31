'''
Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.


Example 1:

Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.

Example 2:

Input: s1 = "delete", s2 = "leet"
Output: 403
Explanation: Deleting "dee" from "delete" to turn the string into "let",
adds 100[d] + 101[e] + 101[e] to the sum.
Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
'''

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = {}

        def compute_cost(i,j) :
            # both empty 
            if i < 0 and j < 0 :
                return 0 

            # saved result exist
            if (i,j) in dp :
                return dp[(i,j)]

            if i < 0 :
                dp[(i,j)] = ord(s2[j]) + compute_cost(i,j-1)
                return dp[(i,j)]

            if j < 0 :
                dp[(i,j)] = ord(s1[i]) + compute_cost(i-1,j)
                return dp[(i,j)]

            if s1[i] == s2[j] :
                dp[(i,j)] = compute_cost(i-1,j-1)
            else:
                dp[(i,j)] = min(
                    ord(s1[i]) + compute_cost(i-1,j),
                    ord(s2[j]) + compute_cost(i,j-1)
                )
            
            return dp[(i,j)]
        return compute_cost(len(s1)-1, len(s2)-1)
        

# class Solution:
#     def minimumDeleteSum(self, s1: str, s2: str) -> int:
#         # recursion give TLE and thus, it has to be converted to dynamic programing

#         # helper function 
#         def computeCost(i,j) :
#             # base case 

#             # case 1 : s1 empty, s2 still remains 
#             if i < 0 :
#                 delete_cost = 0 
#                 for pointer in range (j+1) :
#                     delete_cost += ord(s2[pointer])
#                 return delete_cost 

#             # case 2 : s2 empty, s2 still remains
#             if j < 0 :
#                 delete_cost = 0 
#                 for pointer in range(i+1) :
#                     delete_cost += ord(s1[pointer])
#                 return delete_cost 
            
#             # case 3 : recursion
            
#             # when chars are equal
#             if s1[i] == s2[j] :
#                 return computeCost(i-1,j-1) 
            
#             else :
#                 return min(
#                     ord(s1[i]) + computeCost(i-1,j),
#                     ord(s2[j]) + computeCost(i,j-1),
#                     ord(s1[i]) + ord(s2[j]) + computeCost(i-1,j-1)
#                 )

#         return computeCost(len(s1)-1,len(s2)-1)

