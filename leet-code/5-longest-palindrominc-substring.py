class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.res = ""
        self.res_len = 0 

        def expand (l,r) :
            while l >=0 and r < len(s) and s[l] == s[r] :
                if (r - l + 1) >  self.res_len :
                    self.res = s[l:r+1]
                    self.res_len = r - l + 1
                l -= 1
                r += 1 
        
        for i in range(len(s)) :
            # for odd length 
            expand(i,i)
            # for even length
            expand(i,i+1)

        return self.res