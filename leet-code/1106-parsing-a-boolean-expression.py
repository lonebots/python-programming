'''
A boolean expression is an expression that evaluates to either true or false. It can be in one of the following shapes:

    't' that evaluates to true.
    'f' that evaluates to false.
    '!(subExpr)' that evaluates to the logical NOT of the inner expression subExpr.
    '&(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical AND of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
    '|(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical OR of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.

Given a string expression that represents a boolean expression, return the evaluation of that expression.

It is guaranteed that the given expression is valid and follows the given rules.

 

Example 1:

Input: expression = "&(|(f))"
Output: false
Explanation: 
First, evaluate |(f) --> f. The expression is now "&(f)".
Then, evaluate &(f) --> f. The expression is now "f".
Finally, return false.

Example 2:

Input: expression = "|(f,f,f,t)"
Output: true
Explanation: The evaluation of (false OR false OR false OR true) is true.

Example 3:

Input: expression = "!(&(f,t))"
Output: true
Explanation: 
First, evaluate &(f,t) --> (false AND true) --> false --> f. The expression is now "!(f)".
Then, evaluate !(f) --> NOT false --> true. We return true.

 

Constraints:

    1 <= expression.length <= 2 * 104
    expression[i] is one following characters: '(', ')', '&', '|', '!', 't', 'f', and ','.


'''

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []

        for curr_char in expression:
            if curr_char == ')':
                values = []

                while stack[-1] != "(":
                    values.append(stack.pop())

                stack.pop() # remove "("
                operator = stack.pop() # get the operator

                result = self._evaluate_sub_expression(operator, values)
                stack.append(result)
            elif curr_char != ",":
                stack.append(curr_char)

        return stack[-1] == 't'

    def _evaluate_sub_expression(self, operator, values): 
        if operator == "!":
            return "f" if values[0] == "t" else "t"
        elif operator == "|":
            for value in values: 
                if value == "t":
                    return "t"
            return "f"
        elif operator == "&":
            for value in values:
                if value == "f":
                    return "f"
            return "t"

        return "f" # this point should never be reached