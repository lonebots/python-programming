class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ss = ""
        n = len(s) 
        for i in range(n//2) :
            ss += s[i] 
            if ss * (n // len(ss)) == s :
                return True
        return False