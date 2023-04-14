"""
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".

 

Constraints:

    1 <= s.length <= 1000
    s consists only of lowercase English letters.
"""


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        memo = {}

        def lps(l, r):
            if (l, r) in memo:
                return memo[(l, r)]
            if l > r:
                return 0
            if l == r:
                return 1

            if s[l] == s[r]:
                memo[(l, r)] = lps(l + 1, r - 1) + 2
            else:
                memo[(l, r)] = max(lps(l, r - 1), lps(l + 1, r))
            return memo[(l, r)]

        return lps(0, n - 1)
