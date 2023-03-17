'''
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "3+2*2"
Output: 7

Example 2:

Input: s = " 3/2 "
Output: 1

Example 3:

Input: s = " 3+5 / 2 "
Output: 5

'''

class Solution:
    def calculate(self, s: str) -> int:
        idx = 0 

        curr = prev = res = 0 
        curr_op = '+'

        while idx < len(s) :
            var = s[idx]
            if var.isdigit() :
                while idx < len(s) and s[idx].isdigit() :
                    curr = curr * 10 + int(s[idx])
                    idx += 1 
                    # here we may some times reach the end of the string 
                idx -= 1  # we may loose an operation eg : 1223+132, we may loose + if we didn't decrement idx
                if  curr_op == '+' :
                    res += curr
                    prev = curr
                elif curr_op == '-' :
                    res -= curr 
                    prev = -curr

                # handling / and * 
                elif curr_op == '*' :
                    res -= prev 
                    res += prev * curr 
                    prev = curr * prev
                else : # / division
                    res -= prev
                    res += int(prev / curr) 
                    prev = int(prev / curr) 

                curr = 0 # every time we should reset curr
            elif var != " " :
                curr_op = var
            
            
            idx += 1 

        return res