class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1 :
            return True
        l = 0 
        r = num 
        while l < r : 
            m = (l+r)//2
            if m ** 2 == num :
                return True 
            elif m ** 2 < num :
                l = m + 1 
            else :
                r = m
        return False
        