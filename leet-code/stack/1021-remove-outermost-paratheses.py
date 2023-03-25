'''
A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.

    For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

 

Example 1:

Input: s = "(()())(())"
Output: "()()()"
Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

Example 2:

Input: s = "(()())(())(()(()))"
Output: "()()()()(())"
Explanation: 
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".

Example 3:

Input: s = "()()"
Output: ""
Explanation: 
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".

'''

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        # stack = []
        # res = []
        # for item in s :
        #     if len(stack ) == 0 and item == "(" :
        #         stack.append(item)
        #     elif len(stack) == 1 and item == ")" :
        #         stack.pop()
        #     else :
        #         if item == ")" :
        #             while len(stack) > 1 :
        #                 res.append(stack.pop())
        #             res.append(item)
        #         else :
        #             stack.append(item)

        # print(res)
        # return "".join(res[::-1])

        result = []
        open = 0 
        for item in s :
            if item == "(" and open > 0 :
                result.append(item) 
            if item == ")" and open > 1  :
                result.append(item)
            
            open += 1 if item == "(" else  - 1
        return "".join(result)