'''
Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

    Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
    Each vowel 'a' may only be followed by an 'e'.
    Each vowel 'e' may only be followed by an 'a' or an 'i'.
    Each vowel 'i' may not be followed by another 'i'.
    Each vowel 'o' may only be followed by an 'i' or a 'u'.
    Each vowel 'u' may only be followed by an 'a'.

Since the answer may be too large, return it modulo 10^9 + 7.

 

Example 1:

Input: n = 1
Output: 5
Explanation: All possible strings are: "a", "e", "i" , "o" and "u".

Example 2:

Input: n = 2
Output: 10
Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".

Example 3: 

Input: n = 5
Output: 68
'''

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7

        a, e, i, o, u = 1, 1, 1, 1, 1

        for _ in range(1,n):
            a_next = e 
            e_next = (a + i) % MOD
            i_next = (a + e + o + u ) % MOD
            o_next = (i + u) % MOD
            u_next = a 

            a, e, i, o, u = a_next, e_next, i_next, o_next, u_next

        return (a + e + i + o + u) % MOD