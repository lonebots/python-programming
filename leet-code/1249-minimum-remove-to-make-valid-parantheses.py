'''
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

    It is the empty string, contains only lowercase characters, or
    It can be written as AB (A concatenated with B), where A and B are valid strings, or
    It can be written as (A), where A is a valid string.

 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"

Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.

 

Constraints:

    1 <= s.length <= 105
    s[i] is either'(' , ')', or lowercase English letter.
'''

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        openParanthesesCount = 0
        arr = list(s)

        # forward pass
        for i in range(len(arr)) :
            if arr[i] == "(" :
                openParanthesesCount += 1 
            elif arr[i] == ")" :
                if openParanthesesCount == 0 :
                    arr[i] = "*" 
                else :
                    openParanthesesCount -= 1
        
        # backward pass 
        for i in range(len(arr)-1, -1, -1) :
            if openParanthesesCount > 0 and arr[i] == "(" :
                arr[i] = "*" # mark excess 
                openParanthesesCount -= 1
        
        result = "".join( char for char in arr if char != "*")

        return result 