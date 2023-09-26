'''
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is 
the smallest in lexicographical order
 among all possible results.

 

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
'''

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurance = {}
        stack = []
        visited = set()

        # set the last occurance for each character
        for i in range(len(s)) :
            last_occurance[s[i]] = i 

        for i in range(len(s)) :
            if s[i] not in visited :
                while (stack and stack[-1] > s[i] and last_occurance[stack[-1]] > i) :
                    visited.remove(stack.pop())
                
                stack.append(s[i])
                visited.add(s[i])

        return "".join(stack)        