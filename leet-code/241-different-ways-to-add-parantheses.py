'''
Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.

The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed 104.

 

Example 1:

Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0 
(2-(1-1)) = 2

Example 2:

Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10

 

Constraints:

    1 <= expression.length <= 20
    expression consists of digits and the operator '+', '-', and '*'.
    All the integer values in the input expression are in the range [0, 99].
    The integer values in the input expression do not have a leading '-' or '+' denoting the sign.

'''

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        results = []

        #base case 1 : empty string
        if len(expression) == 0:
            return results

        #base case2 : string has single character; return its integer 
        if len(expression) == 1:
            return [int(expression)]

        
        #base case3 : 2 characters in the expression and first character is digit
        if len(expression) == 2 and expression[0].isdigit():
            return [int(expression)]

        # recursive case 
        for i, current_char in enumerate(expression):
            #skip character is digit 
            if current_char.isdigit():
                continue 

            #split 2 parts left and right 
            left_results = self.diffWaysToCompute(expression[:i])
            right_results = self.diffWaysToCompute(expression[i + 1:])

            #combine the left and right results
            for left_value in left_results:
                for right_value in right_results:
                    # perform the operations based on the current character
                    if current_char == "+":
                        results.append(left_value + right_value)
                    elif current_char == "-":
                        results.append(left_value - right_value)
                    elif current_char == "*":
                        results.append(left_value * right_value)
            

        return results