'''
Given a string s, return the last substring of s in lexicographical order.

 

Example 1:

Input: s = "abab"
Output: "bab"
Explanation: The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"]. The lexicographically maximum substring is "bab".

Example 2:

Input: s = "leetcode"
Output: "tcode"

 

Constraints:

    1 <= s.length <= 4 * 105
    s contains only lowercase English letters.


'''

class Solution:
    def lastSubstring(self, s: str) -> str:
        n = len(s) 
        mmax = max(s)

        candidates = [i for i, c  in enumerate(s) if c == mmax]

        offset = 1

        while len(candidates) > 1 :
            currMax = max(s[i + offset] for i in candidates if i + offset < n ) 
            newCand = []

            for i, start in enumerate(candidates) :
                if i > 0 and candidates[i-1] + offset == start :
                    continue 

                if start + offset < n and s[start + offset] == currMax :
                    newCand.append(start)

            candidates = newCand
            offset += 1 

        return s[candidates[0]:]

        # approach 3 : 1 pointers  --> O(n) solution not possible --> 3 test cases failed 
        # ptr = 0 
        # res = ""
        # while ptr < len(s)  :
        #     if s[ptr:] > res :
        #         res = s[ptr:]

        #     if s[:ptr] > res :
        #         res = s[:ptr]

        #     ptr += 1
        # return res

        # approach 1 : backtracking --> TLE
        # words = []
        # def backtrack(idx,stack) :
        #     if idx == len(s) :
        #         if ''.join(list(stack)) in s :
        #             words.append(''.join(list(stack)))
        #     else :
        #         stack.append(s[idx]) 
        #         backtrack(idx+1,stack)
        #         stack.pop()
        #         backtrack(idx+1,stack)

        # backtrack(0,[])
        # words.sort()
        # print(words)
        # return words[-1]