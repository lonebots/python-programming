class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = {}
        max_length = 0
        i = 0 
        for j in range(len(s)) :
            if s[j] in hashset :
                i = max(i,hashset[s[j]])

            max_length = max(max_length,j - i + 1)
            hashset[s[j]] = j + 1

        return max_length
