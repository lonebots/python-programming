'''
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "1 + 1"
Output: 2

Example 2:

Input: s = " 2-1 + 2 "
Output: 3

Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23

'''
class Solution:
    def calculate(self, s: str) -> int:
        curr = res = 0 
        sign = 1 
        stack = []  # [result,sign]

        for var in s : 
            if var.isdigit() :
                curr = curr * 10 + int(var) 

            elif var  in ['+','-'] : # apply the computation when operation comes
                res += sign * curr 

                sign = 1 if var == "+" else -1 

                curr = 0
            elif var == "(" :
                stack.append(res)
                stack.append(sign)

                sign = 1
                curr = 0
                res = 0
            elif var == ")" :
                res += sign * curr  # handle the last curr value befor encountering a ")"

                res *= stack.pop()  # attack previous sign to curr result
                res += stack.pop()  # add the previous result to the current result

                curr = 0 

        return res + sign * curr # handle the last curr value which is probably at the end of the string, this comes because we update result only when an operator (+ or - ) is occurs.
            

