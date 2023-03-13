class Solution:
    def longestValidParentheses(self, s: str) -> int:
        o, c = 0 , 0 
        max_ = 0

        # forward pass 
        for p in s :
            if p == "(" :
                o += 1 
            else :
                c += 1 
            
            if o == c : 
                max_ = max(max_,2 * c)
            elif c > o :
                o,c = 0,0
        
        o,c = 0,0 # reset
        # backward pass
        for p in s[::-1] :
            if p == "(" :
                c += 1 
            else :
                o += 1

            if o == c :
                max_ =max(max_ , 2 * c)
            elif c > o :
                o,c = 0,0
            
        return max_